# 🛍️ PhoneShop - Web Bán Hàng Điện Thoại Bằng Django

> Một ứng dụng web bán hàng điện thoại hiện đại với **Dark Mystical Theme**, animation mượt mà, và trải nghiệm người dùng tuyệt vời.

![Django](https://img.shields.io/badge/Django-4.2.7-green)
![Python](https://img.shields.io/badge/Python-3.12.1-blue)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.1.3-purple)
![License](https://img.shields.io/badge/License-MIT-red)

## ✨ Tính Năng Nổi Bật

🌙 **Dark Mystical Theme** - Giao diện tối bí ẩn với màu tím & xanh cyan  
🎨 **Animation mượt mà** - Hiệu ứng fade-in, slide-in, glow, pulse  
📱 **Responsive Design** - Hoạt động tốt trên mọi thiết bị  
🔍 **Tìm kiếm & Lọc** - Tìm sản phẩm nhanh chóng  
⭐ **Đánh giá sản phẩm** - Hệ thống sao 5 ngôi  
💰 **Quản lý giá** - Hỗ trợ giá gốc và giảm giá  
🛒 **Giỏ hàng thông minh** - Quản lý sản phẩm dễ dàng  
🛡️ **Xác thực an toàn** - Đăng ký, đăng nhập, hồ sơ cá nhân  
📦 **Quản lý đơn hàng** - Theo dõi, lịch sử mua hàng  
🔐 **Admin Dashboard** - Quản lý toàn bộ hệ thống  

---

## 🚀 Bắt Đầu Nhanh (Quick Start)

### 📋 Yêu Cầu
```
Python 3.12+
pip & virtualenv
Django 4.2.7
```

### ⚡ Cài Đặt & Chạy (3 bước)

**Bước 1: Vào thư mục + Cài đặt**
```bash
cd /workspaces/Phoneshop
pip install -r requirements.txt
```

**Bước 2: Khởi tạo database**
```bash
python manage.py migrate
python create_sample_data.py  # Thêm 10 sản phẩm mẫu
```

**Bước 3: Chạy server**
```bash
python manage.py runserver 0.0.0.0:8000
```

### 🌐 Truy Cập

- **🏠 Website:** http://127.0.0.1:8000/
- **🔐 Admin Panel:** http://127.0.0.1:8000/admin/
- **Username:** admin
- **Password:** admin123456

---

## 📊 Dữ Liệu Mẫu (Sample Data)

Website đã được tải sẵn 10 sản phẩm mẫu từ các thương hiệu hàng đầu:

| Brand | Model | Giá gốc | Khuyến mãi | Rating |
|-------|-------|---------|-----------|--------|
| 🍎 Apple | iPhone 15 Pro Max | 45.99M | 42.99M ↓ | ⭐⭐⭐⭐⭐ |
| 🍎 Apple | iPhone 15 | 27.99M | 25.99M ↓ | ⭐⭐⭐⭐ |
| 🔵 Samsung | Galaxy S24 Ultra | 39.99M | 37.99M ↓ | ⭐⭐⭐⭐⭐ |
| 🔵 Samsung | Galaxy S24 | 24.99M | 22.99M ↓ | ⭐⭐⭐⭐ |
| 🟠 Xiaomi | Xiaomi 14 Ultra | 16.99M | 14.99M ↓ | ⭐⭐⭐⭐ |
| 🟠 Xiaomi | Xiaomi 14 | 11.99M | 9.99M ↓ | ⭐⭐⭐⭐ |

---

## Đây là một ứng dụng web bán hàng điện thoại chuyên nghiệp được phát triển bằng Django. Ứng dụng cung cấp một giải pháp hoàn chỉnh cho việc bán điện thoại trực tuyến.

## 🎯 Tính Năng Chính

### 👥 Quản Lý Người Dùng
- Đăng ký, đăng nhập, đăng xuất
- Quản lý hồ sơ người dùng
- Lịch sử đơn hàng
- Danh sách yêu thích

### 📱 Quản Lý Sản Phẩm
- Danh sách sản phẩm với hình ảnh
- Tìm kiếm, lọc theo danh mục, giá
- Chi tiết sản phẩm với thông số kỹ thuật
- Đánh giá sản phẩm từ khách hàng
- Quản lý hình ảnh sản phẩm
- Giảm giá

### 🛒 Giỏ Hàng & Thanh Toán
- Thêm/xóa sản phẩm vào giỏ hàng
- Cập nhật số lượng
- Tính toán tạm tính, phí vận chuyển, thuế
- Thanh toán với nhiều phương thức (COD, chuyển khoản, Stripe)
- Xác nhận đơn hàng

### 📦 Quản Lý Đơn Hàng
- Tạo đơn hàng
- Theo dõi trạng thái đơn hàng
- Thông tin giao hàng
- Chi tiết thanh toán

### 💳 Giao Diện Quản Trị
- Django Admin tích hợp
- Quản lý danh mục, sản phẩm, đơn hàng
- Quản lý người dùng và đánh giá

## 🚀 Cài Đặt & Chạy

### Yêu Cầu
- Python 3.8+
- pip (bộ quản lý gói Python)
- virtualenv (tùy chọn nhưng được khuyến nghị)

### Các Bước Cài Đặt

#### 1. Clone hoặc Download Dự Án
```bash
cd Phoneshop
```

#### 2. Tạo Virtual Environment (Khuyến Nghị)
```bash
python -m venv venv

# Kích hoạt virtual environment
# Trên Windows:
venv\Scripts\activate

# Trên macOS/Linux:
source venv/bin/activate
```

#### 3. Cài Đặt Các Gói Phụ Thuộc
```bash
pip install -r requirements.txt
```

#### 4. Thiết Lập Biến Môi Trường
```bash
# Copy .env.example thành .env
cp .env.example .env

# Sửa file .env nếu cần
# SECRET_KEY: tạo một key bảo mật
# DEBUG: True cho development, False cho production
```

#### 5. Chạy Database Migrations
```bash
python manage.py migrate
```

#### 6. Tạo Tài Khoản Admin
```bash
python manage.py createsuperuser
```

Nhập các thông tin sau:
- Username: `admin` (hoặc tên khác)
- Email: `admin@example.com`
- Password: `123456` (hoặc mật khẩu khác)

#### 7. Thu Thập Static Files (Tùy Chọn)
```bash
python manage.py collectstatic
```

#### 8. Chạy Development Server
```bash
python manage.py runserver
```

Ứng dụng sẽ chạy tại: `http://127.0.0.1:8000/`
Admin panel: `http://127.0.0.1:8000/admin/`

## 📖 Cách Sử Dụng

### Truy Cập Admin Panel
1. Đi đến `http://127.0.0.1:8000/admin/`
2. Đăng nhập với tài khoản admin đã tạo
3. Tạo các danh mục sản phẩm
4. Thêm sản phẩm điện thoại
5. Quản lý đơn hàng và khách hàng

### Sử Dụng Web Frontend
1. Đi đến trang chủ: `http://127.0.0.1:8000/`
2. Duyệt sản phẩm
3. Đăng ký/Đăng nhập
4. Thêm sản phẩm vào giỏ hàng
5. Thanh toán đơn hàng

## 📁 Cấu Trúc Thư Mục

```
Phoneshop/
├── manage.py                 # Django management script
├── requirements.txt          # Danh sách các gói phụ thuộc
├── .env.example             # Template cho biến môi trường
├── README.md                # Tài liệu này
│
├── phoneshop_project/       # Cấu hình dự án chính
│   ├── __init__.py
│   ├── settings.py          # Cấu hình Django
│   ├── urls.py              # URL chính của dự án
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
│
├── store/                   # Ứng dụng chính (Django app)
│   ├── migrations/          # Database migrations
│   ├── templates/           # HTML templates
│   │   ├── base.html        # Base template
│   │   └── store/           # App templates
│   │       ├── home.html
│   │       ├── product_list.html
│   │       ├── product_detail.html
│   │       ├── cart.html
│   │       ├── checkout.html
│   │       ├── login.html
│   │       ├── register.html
│   │       └── ...
│   ├── static/              # Static files (CSS, JS, images)
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   └── main.js
│   │   └── images/
│   ├── admin.py            # Django Admin configuration
│   ├── apps.py             # App configuration
│   ├── context_processors.py # Template context processors
│   ├── forms.py            # Django Forms
│   ├── models.py           # Database models
│   ├── urls.py             # URL routing
│   └── views.py            # View functions
│
└── media/                  # User uploaded files (sẽ được tạo)
```

## 🗄️ Models (Mô Hình Dữ Liệu)

### Category (Danh Mục)
- Tên danh mục
- Slug (URL friendly)
- Mô tả
- Hình ảnh

### Phone (Điện Thoại)
- Tên sản phẩm
- Thương hiệu
- Mô tả
- Giá gốc / Giá khuyến mãi
- Thông số kỹ thuật (CPU, RAM, Storage, v.v.)
- Hình ảnh
- Rating
- Stock

### CartItem (Mục Giỏ Hàng)
- Người dùng
- Sản phẩm
- Số lượng

### Order (Đơn Hàng)
- Người dùng
- Mã đơn hàng
- Thông tin giao hàng
- Trạng thái
- Phương thức thanh toán
- Chi tiết tính toán

### OrderItem (Mục Đơn Hàng)
- Đơn hàng
- Sản phẩm
- Số lượng
- Giá

### Review (Đánh Giá)
- Sản phẩm
- Người dùng
- Đánh giá (1-5 sao)
- Bình luận

### Wishlist (Danh Sách Yêu Thích)
- Người dùng
- Danh sách sản phẩm

## 🔧 Tùy Chỉnh

### Thay Đổi Tiêu Đề và Branding
Sửa trong `store/templates/base.html`:
```html
<a class="navbar-brand" href="{% url 'store:home' %}">📱 PhoneShop</a>
```

### Cấu Hình Stripe
1. Lấy API key từ Stripe
2. Thêm vào file `.env`:
```
STRIPE_SECRET_KEY=your_secret_key
STRIPE_PUBLIC_KEY=your_public_key
```

### Thay Đổi Phí Vận Chuyển
Trong `store/views.py`, hàm `checkout`:
```python
shipping_cost = Decimal('50000')  # Thay đổi giá trị này
```

### Tùy Chỉnh CSS
Sửa `store/static/css/style.css`

## 🐛 Gỡ Lỗi

### Lỗi: "ModuleNotFoundError"
- Kiểm tra Virtual Environment đã được kích hoạt chưa
- Chạy `pip install -r requirements.txt`

### Lỗi: "No such table"
- Chạy `python manage.py migrate`

### Lỗi: "Static files not found"
- Chạy `python manage.py collectstatic`

### Lỗi: "Port 8000 already in use"
```bash
# Sử dụng port khác
python manage.py runserver 8001
```

## 📚 Thêm Sản Phẩm Qua Admin

1. Đăng nhập Admin Panel: `http://127.0.0.1:8000/admin/`
2. Đi đến "Phones"
3. Nhấp "Add Phone"
4. Điền thông tin:
   - Name: Tên sản phẩm
   - Category: Chọn danh mục
   - Description: Mô tả chi tiết
   - Price: Giá gốc
   - Discount Price: Giá khuyến mãi (tùy chọn)
   - Brand: Thương hiệu
   - Thông số kỹ thuật
   - Image: Tải ảnh chính
   - Stock: Số lượng tồn kho
5. Nhấp "Save"

## 🚀 Deployment (Triển Khai)

### Trên Heroku
```bash
# 1. Install Heroku CLI
# 2. Login
heroku login

# 3. Create app
heroku create your-app-name

# 4. Add environment variables
heroku config:set SECRET_KEY=your_secret_key
heroku config:set DEBUG=False

# 5. Push to Heroku
git push heroku main
```

### Trên VPS/Server
1. Sử dụng Gunicorn hoặc uWSGI
2. Cấu hình Nginx reverse proxy
3. Sử dụng PostgreSQL thay SQLite
4. Thiết lập SSL/HTTPS

## 📝 License

Dự án này được phát hành dưới giấy phép MIT.

## 💬 Hỗ Trợ

Để được hỗ trợ, vui lòng liên hệ:
- Email: support@phoneshop.vn
- Hotline: 1800-1234

## 📌 Ghi Chú

- Ứng dụng này sử dụng SQLite cho development. Trong production, nên sử dụng PostgreSQL hoặc MySQL.
- Hãy đổi `SECRET_KEY` trong production
- Tắt `DEBUG=False` trong production
- Sử dụng HTTPS trong production

---

**Phiên bản:** 1.0.0  
**Cập nhật lần cuối:** 2024