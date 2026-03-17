"""
Script to create sample data for the PhoneShop application
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'phoneshop_project.settings')
django.setup()

from store.models import Category, Phone
from django.contrib.auth.models import User

# Clear existing data
print("Clearing existing data...")
Phone.objects.all().delete()
Category.objects.all().delete()

# Create Categories
print("Creating categories...")
apple_cat = Category.objects.create(
    name="Apple iPhone",
    slug="apple-iphone",
    description="Những chiếc iPhone mới nhất từ Apple với công nghệ tiên tiến nhất"
)

samsung_cat = Category.objects.create(
    name="Samsung Galaxy",
    slug="samsung-galaxy",
    description="Điện thoại Samsung Galaxy với màn hình AMOLED tuyệt vời"
)

xiaomi_cat = Category.objects.create(
    name="Xiaomi",
    slug="xiaomi",
    description="Điện thoại Xiaomi với giá cả phải chăng và hiệu năng mạnh mẽ"
)

# Create Sample Phones
print("Creating sample phones...")

phones_data = [
    {
        "name": "iPhone 15 Pro Max",
        "slug": "iphone-15-pro-max",
        "brand": "Apple",
        "model": "iPhone 15 Pro Max",
        "category": apple_cat,
        "price": 45990000,
        "cpu": "Apple A17 Pro",
        "ram": "8 GB",
        "storage": "256 GB",
        "display": "6.7 inches, 120Hz",
        "camera": "48 MP chính + 12 MP ultra rộng + 12 MP tele",
        "battery": "4685 mAh",
        "os": "iOS 17",
        "description": "iPhone 15 Pro Max là chiếc điện thoại cao cấp nhất từ Apple với chip A17 Pro mạnh mẽ, camera 48MP chất lượng cao, và thiết kế từ titanium",
        "stock": 10,
        "rating": 4.8,
        "discount_price": 42990000
    },
    {
        "name": "iPhone 15",
        "slug": "iphone-15",
        "brand": "Apple",
        "model": "iPhone 15",
        "category": apple_cat,
        "price": 27990000,
        "cpu": "Apple A16 Bionic",
        "ram": "6 GB",
        "storage": "128 GB",
        "display": "6.1 inches, 60Hz",
        "camera": "48 MP chính + 12 MP ultra rộng",
        "battery": "3349 mAh",
        "os": "iOS 17",
        "description": "iPhone 15 với chip A16 Bionic, camera kép Dynamic Island, và giá cả phải chăng hơn Pro Max",
        "stock": 15,
        "rating": 4.6,
        "discount_price": 25990000
    },
    {
        "name": "Samsung Galaxy S24 Ultra",
        "slug": "samsung-s24-ultra",
        "brand": "Samsung",
        "model": "Galaxy S24 Ultra",
        "category": samsung_cat,
        "price": 39990000,
        "cpu": "Snapdragon 8 Gen 3",
        "ram": "12 GB",
        "storage": "256 GB",
        "display": "6.8 inches, 120Hz AMOLED",
        "camera": "200 MP chính + 50 MP tele + 10 MP tele + 10 MP ultra rộng",
        "battery": "5000 mAh",
        "os": "Android 14",
        "description": "Galaxy S24 Ultra với camera 200MP siêu khủng, bút S Pen thông minh, và độ sáng màn hình cao nhất",
        "stock": 8,
        "rating": 4.7,
        "discount_price": 37990000
    },
    {
        "name": "Samsung Galaxy S24",
        "slug": "samsung-s24",
        "brand": "Samsung",
        "model": "Galaxy S24",
        "category": samsung_cat,
        "price": 24990000,
        "cpu": "Snapdragon 8 Gen 3",
        "ram": "8 GB",
        "storage": "256 GB",
        "display": "6.2 inches, 120Hz AMOLED",
        "camera": "50 MP chính + 12 MP tele + 10 MP ultra rộng",
        "battery": "4000 mAh",
        "os": "Android 14",
        "description": "Galaxy S24 với thiết kế tròn trịa, camera tele zoom 3x, và hiệu suất cực mạnh",
        "stock": 12,
        "rating": 4.5,
        "discount_price": 22990000
    },
    {
        "name": "Xiaomi 14 Ultra",
        "slug": "xiaomi-14-ultra",
        "brand": "Xiaomi",
        "model": "Xiaomi 14 Ultra",
        "category": xiaomi_cat,
        "price": 16990000,
        "cpu": "Snapdragon 8 Gen 3",
        "ram": "12 GB",
        "storage": "512 GB",
        "display": "6.73 inches, 120Hz",
        "camera": "50 MP (OIS) + camera tele",
        "battery": "5300 mAh",
        "os": "MIUI 15",
        "description": "Xiaomi 14 Ultra với camera flagship cùng Leica, thiết kế sang trọng, giá cả phải chăng",
        "stock": 20,
        "rating": 4.4,
        "discount_price": 14990000
    },
    {
        "name": "Xiaomi 14",
        "slug": "xiaomi-14",
        "brand": "Xiaomi",
        "model": "Xiaomi 14",
        "category": xiaomi_cat,
        "price": 11990000,
        "cpu": "Snapdragon 8 Gen 3",
        "ram": "8 GB",
        "storage": "256 GB",
        "display": "6.36 inches, 120Hz",
        "camera": "50 MP chính + 50 MP ultra rộng + 50 MP tele",
        "battery": "4610 mAh",
        "os": "MIUI 15",
        "description": "Xiaomi 14 với chip Snapdragon 8 mạnh nhất, camera 50MP, giá chỉ từ 11.99 triệu",
        "stock": 25,
        "rating": 4.3,
        "discount_price": 9990000
    },
    {
        "name": "iPhone 14 Pro",
        "slug": "iphone-14-pro",
        "brand": "Apple",
        "model": "iPhone 14 Pro",
        "category": apple_cat,
        "price": 27460000,
        "cpu": "Apple A16 Bionic",
        "ram": "6 GB",
        "storage": "128 GB",
        "display": "6.1 inches, 120Hz ProMotion",
        "camera": "48 MP chính + 12 MP tele",
        "battery": "3200 mAh",
        "os": "iOS 17",
        "description": "iPhone 14 Pro với chip A16 Bionic, camera Pro tele 3x, Dynamic Island",
        "stock": 7,
        "rating": 4.5,
        "discount_price": 24990000
    },
    {
        "name": "Samsung Galaxy A55",
        "slug": "samsung-a55",
        "brand": "Samsung",
        "model": "Galaxy A55",
        "category": samsung_cat,
        "price": 8990000,
        "cpu": "Exynos 1480",
        "ram": "8 GB",
        "storage": "256 GB",
        "display": "6.5 inches, 120Hz AMOLED",
        "camera": "50 MP + 12 MP + 12 MP + 5 MP",
        "battery": "5000 mAh",
        "os": "Android 14",
        "description": "Galaxy A55 với camera 4 ống kính, màn hình AMOLED 120Hz, pin 5000mAh, giá bình dân",
        "stock": 30,
        "rating": 4.2,
        "discount_price": 7990000
    },
    {
        "name": "Xiaomi Redmi Note 13",
        "slug": "xiaomi-redmi-note-13",
        "brand": "Xiaomi",
        "model": "Redmi Note 13",
        "category": xiaomi_cat,
        "price": 5990000,
        "cpu": "MediaTek Helio G99",
        "ram": "6 GB",
        "storage": "128 GB",
        "display": "6.67 inches, 120Hz",
        "camera": "50 MP + 8 MP ultra rộng",
        "battery": "5000 mAh",
        "os": "MIUI 14",
        "description": "Redmi Note 13 với màn hình LCD 120Hz, pin 5000mAh, giá siêu rẻ chỉ 5.99 triệu",
        "stock": 35,
        "rating": 4.0,
        "discount_price": 4990000
    },
    {
        "name": "Samsung Galaxy Z Fold 5",
        "slug": "samsung-z-fold-5",
        "brand": "Samsung",
        "model": "Galaxy Z Fold 5",
        "category": samsung_cat,
        "price": 39990000,
        "cpu": "Snapdragon 8 Gen 2",
        "ram": "12 GB",
        "storage": "256 GB",
        "display": "7.6 inches (folded), 17.3 inches (unfolded)",
        "camera": "50 MP + 10 MP + 12 MP",
        "battery": "4400 mAh",
        "os": "Android 13",
        "description": "Galaxy Z Fold 5 - chiếc điện thoại gập cải tiến với bản lề mở rộng, ít nếp gập",
        "stock": 5,
        "rating": 4.6,
        "discount_price": 36990000
    }
]

# Create phones
for phone_data in phones_data:
    phone = Phone.objects.create(**phone_data)
    print(f"✓ Created: {phone.name}")

print("\n✅ Sample data created successfully!")
print(f"Total categories: {Category.objects.count()}")
print(f"Total phones: {Phone.objects.count()}")
