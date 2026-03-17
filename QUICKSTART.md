# Quick Start Guide - Hướng Dẫn Bắt Đầu Nhanh

## ⚡ Bắt Đầu Nhanh (5 phút)

### 1. Cài Đặt Thư Viện
```bash
pip install -r requirements.txt
```

### 2. Tạo Database & Admin
```bash
python manage.py migrate
python manage.py createsuperuser
```
Nhập: username=`admin`, password=`123456`

### 3. Chạy Server
```bash
python manage.py runserver
```

### 4. Truy Cập
- **Trang chủ**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

---

## 📱 Thêm Sản Phẩm đầu Tiên

### Qua Admin Panel:

1. Đi đến `http://127.0.0.1:8000/admin/`
2. Đăng nhập với admin account
3. Nhấp **Category** → Add Category
   - Name: `iPhone`
   - Slug: `iphone` (tự động)
4. Nhấp **Phones** → Add Phone
   - Name: `iPhone 15 Pro`
   - Category: `iPhone`
   - Brand: `Apple`
   - Price: `25000000`
   - Stock: `10`
   - Chọn hình ảnh
5. Nhấp **Save**

### Qua Django Shell:

```bash
python manage.py shell
```

```python
from store.models import Category, Phone
from decimal import Decimal

# Tạo danh mục
cat, _ = Category.objects.get_or_create(
    name='Samsung',
    defaults={'slug': 'samsung', 'description': 'Samsung phones'}
)

# Thêm sản phẩm
Phone.objects.create(
    name='Samsung Galaxy S24',
    slug='samsung-galaxy-s24',
    category=cat,
    brand='Samsung',
    model='S24',
    price=Decimal('23000000'),
    stock=15,
    description='Flagship Samsung phone',
    image='path/to/image.jpg'
)

exit()
```

---

## 👤 Tạo Tài Khoản Khách Hàng

### Qua Web:
1. Nhấp **Đăng ký** ở Navbar
2. Điền thông tin và nhấp **Đăng ký**

### Qua Django Shell:
```bash
python manage.py shell
```

```python
from django.contrib.auth.models import User

User.objects.create_user(
    username='customer1',
    email='customer1@example.com',
    password='password123'
)

exit()
```

---

## 🛍️ Thực Hiện Mua Hàng (Test)

1. Truy cập: http://127.0.0.1:8000/
2. **Đăng ký / Đăng nhập**
3. **Duyệt sản phẩm** - Nhấp vào sản phẩm
4. **Thêm vào giỏ** - Nhập số lượng, nhấp nút
5. **Xem giỏ hàng** - Kiểm tra sản phẩm
6. **Thanh toán** - Nhập thông tin giao hàng
7. **Xác nhận** - Hoàn thành đặt hàng

---

## 📊 Quản Lý Đơn Hàng (Admin)

1. Truy cập: http://127.0.0.1:8000/admin/
2. Đi tới **Orders**
3. Nhấp vào đơn hàng cần quản lý
4. Thay đổi **Status**:
   - `pending` → Chờ xác nhận
   - `confirmed` → Đã xác nhận
   - `processing` → Đang xử lý
   - `shipped` → Đã gửi
   - `delivered` → Đã giao hàng
   - `cancelled` → Đã hủy

---

## 🔧 Cấu Hình Tùy Chỉnh

### Thay Đổi Tên Shop
File: `store/templates/base.html`
```html
<a class="navbar-brand" href="{% url 'store:home' %}">
    📱 MyPhoneShop  <!-- Thay đổi tên ở đây -->
</a>
```

### Thay Đổi Phí Vận Chuyển
File: `store/views.py` (hàm `checkout`)
```python
shipping_cost = Decimal('50000')  # Thay đổi con số này
```

### Thay Đổi Thuế
File: `store/views.py` (hàm `checkout`)
```python
tax = (subtotal + shipping_cost) * Decimal('0.1')  # 10%
```

---

## 🐛 Thường Gặp Lỗi

**Lỗi 1: "No such table: store_phone"**
```bash
python manage.py migrate
```

**Lỗi 2: "Port 8000 already in use"**
```bash
python manage.py runserver 8001
```

**Lỗi 3: Import lỗi Django**
```bash
pip install -r requirements.txt
```

**Lỗi 4: Static files không hiển thị**
```bash
python manage.py collectstatic
```

---

## 📁 File Quan Trọng

| File | Mô Tả |
|------|-------|
| `store/models.py` | Database models |
| `store/views.py` | Business logic |
| `store/forms.py` | Form validation |
| `store/templates/base.html` | Layout chính |
| `store/static/css/style.css` | CSS styling |
| `phoneshop_project/settings.py` | Cấu hình Django |

---

## 🌐 URLs Chính

```
/                           - Trang chủ
/products/                  - Danh sách sản phẩm
/category/<slug>/           - Sản phẩm theo danh mục
/product/<slug>/            - Chi tiết sản phẩm
/cart/                      - Giỏ hàng
/checkout/                  - Thanh toán
/orders/                    - Lịch sử đơn hàng
/wishlist/                  - Danh sách yêu thích
/login/                     - Đăng nhập
/register/                  - Đăng ký
/profile/                   - Hồ sơ người dùng
/about/                     - Về chúng tôi
/contact/                   - Liên hệ
/admin/                     - Admin panel
```

---

## 💡 Mẹo Hữu Ích

### Tạo dữ liệu test
```bash
python manage.py shell < fixtures/sample_data.py
```

### Xóa tất cả dữ liệu
```bash
python manage.py flush
```

### Backup database
```bash
cp db.sqlite3 db.sqlite3.backup
```

### Restore database
```bash
cp db.sqlite3.backup db.sqlite3
```

### Xem SQL queries
```python
from django.db import connection
from django.test.utils import CaptureQueriesContext

with CaptureQueriesContext(connection) as context:
    phones = Phone.objects.filter(price__gte=10000000)

for query in context:
    print(query['sql'])
```

---

## 📚 Tài Liệu Liên Quan

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Models](https://docs.djangoproject.com/en/4.2/topics/db/models/)
- [Django Views](https://docs.djangoproject.com/en/4.2/topics/http/views/)
- [Django Templates](https://docs.djangoproject.com/en/4.2/topics/templates/)

---

**Cần giúp đỡ? Xem [COMMANDS.md](COMMANDS.md) để có thêm lệnh.**
