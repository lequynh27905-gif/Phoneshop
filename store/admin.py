from django.contrib import admin
from .models import Category, Phone, CartItem, Order, OrderItem, Review, Wishlist

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'stock', 'rating', 'is_active', 'created_at')
    list_filter = ('category', 'brand', 'is_active', 'condition', 'created_at')
    search_fields = ('name', 'brand', 'model')
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        ('Thông tin cơ bản', {
            'fields': ('name', 'slug', 'category', 'description', 'brand', 'model')
        }),
        ('Giá', {
            'fields': ('price', 'discount_price')
        }),
        ('Thông tin kỹ thuật', {
            'fields': ('cpu', 'ram', 'storage', 'display', 'camera', 'battery', 'os'),
            'classes': ('collapse',)
        }),
        ('Hình ảnh', {
            'fields': ('image', 'image2', 'image3')
        }),
        ('Khác', {
            'fields': ('condition', 'stock', 'rating', 'review_count', 'is_active')
        }),
    )


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'quantity', 'added_at')
    list_filter = ('added_at',)
    search_fields = ('user__username', 'phone__name')


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'user', 'total', 'status', 'payment_status', 'created_at')
    list_filter = ('status', 'payment_status', 'payment_method', 'created_at')
    search_fields = ('order_number', 'user__username', 'email')
    inlines = [OrderItemInline]
    readonly_fields = ('order_number', 'created_at', 'updated_at')
    fieldsets = (
        ('Thông tin đơn hàng', {
            'fields': ('order_number', 'user', 'status', 'created_at', 'updated_at')
        }),
        ('Thông tin người nhận', {
            'fields': ('full_name', 'email', 'phone', 'address', 'city', 'country', 'postal_code')
        }),
        ('Thanh toán', {
            'fields': ('payment_method', 'payment_status', 'subtotal', 'shipping_cost', 'tax', 'total')
        }),
        ('Ghi chú', {
            'fields': ('notes',)
        }),
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('phone', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('phone__name', 'user__username', 'comment')


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_count')
    search_fields = ('user__username',)
    
    def phone_count(self, obj):
        return obj.phones.count()
    phone_count.short_description = 'Số sản phẩm'
