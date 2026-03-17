from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg, Count
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.utils import timezone
from decimal import Decimal
import uuid

from .models import Phone, Category, CartItem, Order, OrderItem, Review, Wishlist
from .forms import UserRegistrationForm, UserUpdateForm, ReviewForm, CheckoutForm, SearchForm


# ===== HOME & PRODUCT VIEWS =====
def home(request):
    """Trang chủ"""
    categories = Category.objects.all()
    featured_phones = Phone.objects.filter(is_active=True).order_by('-rating')[:6]
    new_phones = Phone.objects.filter(is_active=True).order_by('-created_at')[:6]
    
    context = {
        'featured_phones': featured_phones,
        'new_phones': new_phones,
        'categories': categories,
    }
    return render(request, 'store/home.html', context)


def product_list(request):
    """Danh sách sản phẩm"""
    phones = Phone.objects.filter(is_active=True)
    categories = Category.objects.all()
    form = SearchForm(request.GET or None)
    
    # Tìm kiếm
    query = request.GET.get('q', '')
    if query:
        phones = phones.filter(
            Q(name__icontains=query) |
            Q(brand__icontains=query) |
            Q(description__icontains=query)
        )
    
    # Lọc theo danh mục
    category_id = request.GET.get('category')
    if category_id:
        phones = phones.filter(category_id=category_id)
    
    # Lọc theo giá
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    
    if min_price:
        phones = phones.filter(price__gte=min_price)
    if max_price:
        phones = phones.filter(price__lte=max_price)
    
    # Sắp xếp
    sort_by = request.GET.get('sort', 'newest')
    if sort_by == 'price_low':
        phones = phones.order_by('price')
    elif sort_by == 'price_high':
        phones = phones.order_by('-price')
    elif sort_by == 'rating':
        phones = phones.order_by('-rating')
    else:
        phones = phones.order_by('-created_at')
    
    context = {
        'phones': phones,
        'categories': categories,
        'form': form,
        'query': query,
    }
    return render(request, 'store/product_list.html', context)


def category_list(request, slug):
    """Danh sách sản phẩm theo danh mục"""
    category = get_object_or_404(Category, slug=slug)
    phones = category.phones.filter(is_active=True)
    categories = Category.objects.all()
    
    context = {
        'category': category,
        'phones': phones,
        'categories': categories,
    }
    return render(request, 'store/category_list.html', context)


def product_detail(request, slug):
    """Chi tiết sản phẩm"""
    phone = get_object_or_404(Phone, slug=slug)
    related_phones = Phone.objects.filter(
        category=phone.category,
        is_active=True
    ).exclude(id=phone.id)[:4]
    reviews = phone.reviews.all()
    
    has_reviewed = False
    if request.user.is_authenticated:
        has_reviewed = phone.reviews.filter(user=request.user).exists()
    
    context = {
        'phone': phone,
        'related_phones': related_phones,
        'reviews': reviews,
        'has_reviewed': has_reviewed,
        'review_form': ReviewForm(),
    }
    return render(request, 'store/product_detail.html', context)


# ===== CART VIEWS =====
@login_required
def cart(request):
    """Giỏ hàng"""
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.get_total_price() for item in cart_items)
    
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'items_count': cart_items.count(),
    }
    return render(request, 'store/cart.html', context)


@login_required
@require_POST
def add_to_cart(request):
    """Thêm vào giỏ hàng"""
    phone_id = request.POST.get('phone_id')
    quantity = int(request.POST.get('quantity', 1))
    
    phone = get_object_or_404(Phone, id=phone_id)
    
    if phone.stock < quantity:
        return JsonResponse({
            'success': False,
            'message': 'Số lượng không đủ'
        })
    
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        phone=phone,
        defaults={'quantity': quantity}
    )
    
    if not created:
        cart_item.quantity += quantity
        if cart_item.quantity > phone.stock:
            cart_item.quantity = phone.stock
        cart_item.save()
    
    return JsonResponse({
        'success': True,
        'message': f'Đã thêm {phone.name} vào giỏ hàng',
        'cart_count': CartItem.objects.filter(user=request.user).count()
    })


@login_required
@require_POST
def remove_from_cart(request, item_id):
    """Xóa khỏi giỏ hàng"""
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    
    return redirect('store:cart')


@login_required
@require_POST
def update_cart_quantity(request, item_id):
    """Cập nhật số lượng giỏ hàng"""
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    quantity = int(request.POST.get('quantity', 1))
    
    if quantity > 0 and quantity <= cart_item.phone.stock:
        cart_item.quantity = quantity
        cart_item.save()
    
    return redirect('store:cart')


@login_required
def clear_cart(request):
    """Xóa toàn bộ giỏ hàng"""
    CartItem.objects.filter(user=request.user).delete()
    return redirect('store:cart')


# ===== ORDER VIEWS =====
@login_required
def checkout(request):
    """Thanh toán"""
    cart_items = CartItem.objects.filter(user=request.user)
    
    if not cart_items.exists():
        messages.error(request, 'Giỏ hàng của bạn trống!')
        return redirect('store:cart')
    
    subtotal = sum(item.get_total_price() for item in cart_items)
    shipping_cost = Decimal('50000') if subtotal > 0 else Decimal('0')
    tax = (subtotal + shipping_cost) * Decimal('0.1')
    total = subtotal + shipping_cost + tax
    
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.order_number = generate_order_number()
            order.subtotal = subtotal
            order.shipping_cost = shipping_cost
            order.tax = tax
            order.total = total
            order.save()
            
            # Tạo order items
            for cart_item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    phone=cart_item.phone,
                    quantity=cart_item.quantity,
                    price=cart_item.phone.get_price_display()
                )
                # Cập nhật stock
                cart_item.phone.stock -= cart_item.quantity
                cart_item.phone.save()
            
            # Xóa giỏ hàng
            cart_items.delete()
            
            messages.success(request, 'Đặt hàng thành công!')
            return redirect('store:order_confirmation', order_number=order.order_number)
    else:
        form = CheckoutForm(initial={
            'full_name': f"{request.user.first_name} {request.user.last_name}".strip() or request.user.username,
            'email': request.user.email,
        })
    
    context = {
        'form': form,
        'cart_items': cart_items,
        'subtotal': subtotal,
        'shipping_cost': shipping_cost,
        'tax': tax,
        'total': total,
    }
    return render(request, 'store/checkout.html', context)


def order_confirmation(request, order_number):
    """Xác nhận đơn hàng"""
    order = get_object_or_404(Order, order_number=order_number)
    
    if order.user != request.user and not request.user.is_staff:
        return redirect('store:home')
    
    context = {'order': order}
    return render(request, 'store/order_confirmation.html', context)


@login_required
def order_history(request):
    """Lịch sử đơn hàng"""
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    
    context = {'orders': orders}
    return render(request, 'store/order_history.html', context)


@login_required
def order_detail(request, order_number):
    """Chi tiết đơn hàng"""
    order = get_object_or_404(Order, order_number=order_number)
    
    if order.user != request.user and not request.user.is_staff:
        return redirect('store:home')
    
    context = {'order': order}
    return render(request, 'store/order_detail.html', context)


def generate_order_number():
    """Tạo mã đơn hàng"""
    return f"ORDER-{timezone.now().strftime('%Y%m%d')}-{str(uuid.uuid4())[:8].upper()}"


# ===== REVIEW VIEWS =====
@login_required
@require_POST
def add_review(request, slug):
    """Thêm đánh giá"""
    phone = get_object_or_404(Phone, slug=slug)
    
    # Kiểm tra xem user có purchase phone này không
    has_purchased = OrderItem.objects.filter(
        order__user=request.user,
        phone=phone
    ).exists()
    
    if not has_purchased:
        messages.error(request, 'Bạn phải mua sản phẩm này trước khi đánh giá')
        return redirect('store:product_detail', slug=slug)
    
    form = ReviewForm(request.POST)
    if form.is_valid():
        review, created = Review.objects.get_or_create(
            phone=phone,
            user=request.user,
            defaults={
                'rating': form.cleaned_data['rating'],
                'comment': form.cleaned_data['comment']
            }
        )
        
        if not created:
            review.rating = form.cleaned_data['rating']
            review.comment = form.cleaned_data['comment']
            review.save()
        
        # Cập nhật rating trung bình
        avg_rating = phone.reviews.aggregate(Avg('rating'))['rating__avg'] or 0
        phone.rating = avg_rating
        phone.review_count = phone.reviews.count()
        phone.save()
        
        messages.success(request, 'Đánh giá của bạn đã được lưu')
    
    return redirect('store:product_detail', slug=slug)


# ===== WISHLIST VIEWS =====
@login_required
def wishlist(request):
    """Danh sách yêu thích"""
    wishlist_obj, created = Wishlist.objects.get_or_create(user=request.user)
    phones = wishlist_obj.phones.all()
    
    context = {'phones': phones}
    return render(request, 'store/wishlist.html', context)


@login_required
@require_POST
def add_to_wishlist(request, phone_id):
    """Thêm vào danh sách yêu thích"""
    phone = get_object_or_404(Phone, id=phone_id)
    wishlist_obj, created = Wishlist.objects.get_or_create(user=request.user)
    
    if phone in wishlist_obj.phones.all():
        wishlist_obj.phones.remove(phone)
        message = 'Đã xóa khỏi danh sách yêu thích'
    else:
        wishlist_obj.phones.add(phone)
        message = 'Đã thêm vào danh sách yêu thích'
    
    return JsonResponse({'success': True, 'message': message})


@login_required
def remove_from_wishlist(request, phone_id):
    """Xóa khỏi danh sách yêu thích"""
    phone = get_object_or_404(Phone, id=phone_id)
    wishlist_obj, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist_obj.phones.remove(phone)
    
    return redirect('store:wishlist')


# ===== AUTH VIEWS =====
def register(request):
    """Đăng ký"""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Đăng ký thành công!')
            return redirect('store:home')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'store/register.html', {'form': form})


def login_view(request):
    """Đăng nhập"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'store:home')
            messages.success(request, 'Đăng nhập thành công!')
            return redirect(next_url)
        else:
            messages.error(request, 'Tên đăng nhập hoặc mật khẩu không đúng')
    
    return render(request, 'store/login.html')


@login_required
def logout_view(request):
    """Đăng xuất"""
    logout(request)
    messages.success(request, 'Đăng xuất thành công!')
    return redirect('store:home')


# ===== USER PROFILE VIEWS =====
@login_required
def profile(request):
    """Hồ sơ người dùng"""
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cập nhật hồ sơ thành công!')
            return redirect('store:profile')
    else:
        form = UserUpdateForm(instance=request.user)
    
    context = {'form': form}
    return render(request, 'store/profile.html', context)


# ===== OTHER VIEWS =====
def about(request):
    """Trang về chúng tôi"""
    return render(request, 'store/about.html')


def contact(request):
    """Trang liên hệ"""
    if request.method == 'POST':
        messages.success(request, 'Cảm ơn bạn đã liên hệ. Chúng tôi sẽ phản hồi sớm!')
        return redirect('store:contact')
    return render(request, 'store/contact.html')
