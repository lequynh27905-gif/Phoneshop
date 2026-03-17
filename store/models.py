from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.validators import MinValueValidator

class Category(models.Model):
    """Danh mục sản phẩm điện thoại"""
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Phone(models.Model):
    """Model cho sản phẩm điện thoại"""
    CONDITION_CHOICES = (
        ('new', 'Mới'),
        ('used', 'Đã sử dụng'),
        ('refurbished', 'Tái tạo'),
    )

    name = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='phones')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0)])
    
    # Thông tin kỹ thuật
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    cpu = models.CharField(max_length=100, blank=True)
    ram = models.CharField(max_length=50, blank=True)
    storage = models.CharField(max_length=50, blank=True)
    display = models.CharField(max_length=100, blank=True)
    camera = models.CharField(max_length=100, blank=True)
    battery = models.CharField(max_length=100, blank=True)
    os = models.CharField(max_length=100, blank=True)
    
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='new')
    stock = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to='phones/')
    image2 = models.ImageField(upload_to='phones/', null=True, blank=True)
    image3 = models.ImageField(upload_to='phones/', null=True, blank=True)
    
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    review_count = models.IntegerField(default=0)
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['brand']),
            models.Index(fields=['category']),
        ]

    def __str__(self):
        return self.name

    def get_discount_percentage(self):
        if self.discount_price:
            return int(((self.price - self.discount_price) / self.price) * 100)
        return 0

    def get_price_display(self):
        return self.discount_price if self.discount_price else self.price

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class CartItem(models.Model):
    """Mục trong giỏ hàng"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'phone')
        ordering = ['-added_at']

    def __str__(self):
        return f"{self.user.username} - {self.phone.name}"

    def get_total_price(self):
        return self.phone.get_price_display() * self.quantity


class Order(models.Model):
    """Model cho đơn hàng"""
    STATUS_CHOICES = (
        ('pending', 'Chờ xác nhận'),
        ('confirmed', 'Đã xác nhận'),
        ('processing', 'Đang xử lý'),
        ('shipped', 'Đã gửi'),
        ('delivered', 'Đã giao hàng'),
        ('cancelled', 'Đã hủy'),
    )

    PAYMENT_CHOICES = (
        ('cod', 'Thanh toán khi nhận hàng'),
        ('bank_transfer', 'Chuyển khoản ngân hàng'),
        ('stripe', 'Stripe'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    order_number = models.CharField(max_length=20, unique=True)
    
    # Thông tin người nhận
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='Việt Nam')
    postal_code = models.CharField(max_length=20, blank=True)
    
    # Thông tin đơn hàng
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default='cod')
    payment_status = models.BooleanField(default=False)
    
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    notes = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    shipped_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['order_number']),
            models.Index(fields=['user']),
            models.Index(fields=['status']),
        ]

    def __str__(self):
        return f"Order {self.order_number}"


class OrderItem(models.Model):
    """Mục trong đơn hàng"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.order.order_number} - {self.phone.name}"

    def get_total_price(self):
        return self.price * self.quantity


class Review(models.Model):
    """Model cho đánh giá sản phẩm"""
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('phone', 'user')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.phone.name} - {self.user.username} ({self.rating}⭐)"


class Wishlist(models.Model):
    """Model cho danh sách yêu thích"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wishlist')
    phones = models.ManyToManyField(Phone, related_name='wishlists')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Wishlist"
