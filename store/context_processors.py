from .models import CartItem

def cart_counter(request):
    """Context processor để hiển thị số lượng sản phẩm trong giỏ hàng"""
    cart_count = 0
    
    if request.user.is_authenticated:
        cart_count = CartItem.objects.filter(user=request.user).count()
    
    return {'cart_count': cart_count}
