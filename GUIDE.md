# 📱 PhoneShop - Hướng dẫn sử dụng

## 🎯 Giới thiệu

PhoneShop là một ứng dụng web bán hàng điện thoại hiệu suất cao được xây dựng bằng Django framework. Website này cung cấp giao diện bóng bẩy với chủ đề tối bí ẩn (Dark Mystical Theme), tính năng mua sắm đầy đủ, và trải nghiệm người dùng tuyệt vời.

## 🚀 Tính năng chính

### 1. **Giao diện người dùng (UI/UX)**
- 🌙 Chủ đề tối bí ẩn với màu tím (#6f42c1) và xanh cyan (#00d4ff)
- ✨ Hiệu ứng animation mượt mà (fade-in, slide-in, glow, pulse)
- 📱 Thiết kế responsive cho mọi kích thước màn hình
- 🎨 Font Awesome icons và Bootstrap 5 styling hiện đại

### 2. **Quản lý sản phẩm**
- 📂 Danh mục sản phẩm (Apple iPhone, Samsung Galaxy, Xiaomi)
- 🔍 Tìm kiếm và lọc sản phẩm
- ⭐ Hệ thống đánh giá 5 sao
- 💰 Hỗ trợ giá gốc và giá giảm giá
- 📊 Hiển thị chi tiết kỹ thuật (CPU, RAM, Storage, Camera, v.v.)

### 3. **Hệ thống giỏ hàng**
- 🛒 Thêm/xóa sản phẩm vào giỏ
- 🔢 Quản lý số lượng sản phẩm
- 💳 Tính toán tổng tiền tự động
- ❤️ Danh sách yêu thích

### 4. **Đặt hàng và thanh toán**
- 📦 Quy trình checkout đơn giản
- 📍 Nhập thông tin giao hàng
- 💳 Hỗ trợ thanh toán (chuẩn bị tích hợp Stripe)
- 🧾 Xem chi tiết đơn hàng

### 5. **Quản trị admin**
- 🔐 Admin panel tại `/admin/`
- 📋 Quản lý sản phẩm, danh mục, đơn hàng, bình luận
- 👥 Quản lý người dùng
- 📊 Bộ lọc và tìm kiếm nâng cao

### 6. **Xác thực người dùng**
- 📝 Đăng ký tài khoản mới
- 🔐 Đăng nhập/Đăng xuất
- 👤 Hồ sơ cá nhân
- 📜 Lịch sử đơn hàng

### 7. **Đánh giá và bình luận**
- ⭐ Hệ thống đánh giá 5 sao
- 💬 Bình luận sản phẩm
- 📱 Hiển thị đánh giá trên trang sản phẩm

## 📊 Dữ liệu mẫu

Website đã được tải sẵn với **10 sản phẩm mẫu** từ các thương hiệu nổi tiếng:

### Apple iPhone
- iPhone 15 Pro Max - 45,990,000₫ (giảm xuống 42,990,000₫)
- iPhone 15 - 27,990,000₫ (giảm xuống 25,990,000₫)
- iPhone 14 Pro - 27,460,000₫ (giảm xuống 24,990,000₫)

### Samsung Galaxy
- Galaxy S24 Ultra - 39,990,000₫ (giảm xuống 37,990,000₫)
- Galaxy S24 - 24,990,000₫ (giảm xuống 22,990,000₫)
- Galaxy A55 - 8,990,000₫ (giảm xuống 7,990,000₫)
- Galaxy Z Fold 5 - 39,990,000₫ (giảm xuống 36,990,000₫)

### Xiaomi
- Xiaomi 14 Ultra - 16,990,000₫ (giảm xuống 14,990,000₫)
- Xiaomi 14 - 11,990,000₫ (giảm xuống 9,990,000₫)
- Redmi Note 13 - 5,990,000₫ (giảm xuống 4,990,000₫)

## 🔑 Thông tin đăng nhập Admin

```
Username: admin
Password: admin123456
URL: http://127.0.0.1:8000/admin/
```

## 📍 Các trang chính

| Trang | URL | Mô tả |
|-------|-----|-------|
| Trang chủ | `/` | Sản phẩm nổi bật, mới nhất, danh mục |
| Danh sách sản phẩm | `/products/` | Tất cả sản phẩm với tìm kiếm/lọc |
| Chi tiết sản phẩm | `/product/{slug}/` | Thông tin chi tiết, đánh giá, bình luận |
| Giỏ hàng | `/cart/` | Các sản phẩm trong giỏ |
| Thanh toán | `/checkout/` | Nhập thông tin giao hàng, xác nhận |
| Lịch sử đơn | `/orders/` | Các đơn hàng đã đặt |
| Danh sách yêu thích | `/wishlist/` | Sản phẩm đã lưu |
| Đăng nhập | `/login/` | Xác thực người dùng |
| Đăng ký | `/register/` | Tạo tài khoản mới |
| Hồ sơ | `/profile/` | Thông tin cá nhân |
| Về chúng tôi | `/about/` | Thông tin công ty |
| Liên hệ | `/contact/` | Trang liên hệ |

## 🎨 Cấu trúc giao diện

### Màu sắc (Dark Mystical Theme)
- **Primary Color**: #6f42c1 (Purple)
- **Accent Color**: #00d4ff (Cyan)
- **Dark Background**: #0f172a
- **Text Light**: #f1f5f9
- **Warning/Price**: #f59e0b (Amber)

### Hiệu ứng animation
- **fadeInUp**: Fade in từ dưới lên
- **slideInLeft**: Trượt vào từ trái
- **glow**: Hiệu ứng phát sáng
- **pulse**: Nhịp xung
- **spin**: Quay vòng (spinner)

## 🛠️ Công nghệ sử dụng

### Backend
- **Django 4.2.7** - Web framework Python
- **SQLite3** - Database (dev)
- **Pillow 10.1.0** - Xử lý ảnh
- **django-crispy-forms** - Form rendering
- **crispy-bootstrap5** - Bootstrap 5 integration
- **stripe** - Payment processing (optional)

### Frontend
- **Bootstrap 5.1.3** - CSS framework
- **Font Awesome 6.4.0** - Icons
- **Vanilla JavaScript** - Interactivity
- **CSS3** - Styling & animations

### Tools & Libraries
- **python-decouple** - Environment variables
- **django-admin** - Admin interface

## 📦 Cấu trúc dự án

```
Phoneshop/
├── phoneshop_project/
│   ├── settings.py          # Cấu hình Django
│   ├── urls.py              # URL routing chính
│   └── wsgi.py              # WSGI config
├── store/
│   ├── models.py            # Database models
│   ├── views.py             # Business logic
│   ├── forms.py             # Django forms
│   ├── urls.py              # URL routing app
│   ├── admin.py             # Admin config
│   ├── templates/store/     # HTML templates
│   └── static/
│       ├── css/style.css    # Styling chính
│       └── js/main.js       # JavaScript
├── manage.py                # Django management
├── create_sample_data.py     # Script tạo dữ liệu mẫu
└── requirements.txt         # Dependencies

Models:
├── Category      # Danh mục sản phẩm
├── Phone         # Sản phẩm điện thoại
├── CartItem      # Mục trong giỏ
├── Order         # Đơn hàng
├── OrderItem     # Mục trong đơn
├── Review        # Đánh giá/bình luận
└── Wishlist      # Danh sách yêu thích
```

## 🔧 Cài đặt và chạy

### 1. Clone repository
```bash
cd /workspaces/Phoneshop
```

### 2. Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### 3. Chạy migrations
```bash
python manage.py migrate
```

### 4. Tải dữ liệu mẫu (optional)
```bash
python create_sample_data.py
```

### 5. Chạy development server
```bash
python manage.py runserver 0.0.0.0:8000
```

### 6. Truy cập website
- **Website**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## 💡 Các tính năng nâng cao

### Search & Filter
- Tìm kiếm theo tên sản phẩm
- Lọc theo danh mục
- Sắp xếp theo giá, đánh giá, mới nhất

### Notifications
- Thông báo thêm sản phẩm vào giỏ
- Thông báo lỗi/thành công
- Toast notifications tự động đóng

### Wishlist
- Thêm/xóa sản phẩm yêu thích
- Hiển thị icon tim trên sản phẩm
- Quản lý danh sách từ trang riêng

### Reviews
- Đánh giá 1-5 sao
- Bình luận text
- Hiển thị rating trung bình
- Chỉ người mua mới được đánh giá

## 🐛 Lỗi thường gặp

### "No such table" error
**Giải pháp**: Chạy `python manage.py migrate`

### Image not found
**Giải pháp**: Các sản phẩm không có ảnh sẽ hiển thị icon điện thoại placeholder

### CSRF token missing
**Giải pháp**: Đảm bảo form có `{% csrf_token %}`

## 📝 Notes quan trọng

1. **Database**: Sử dụng SQLite3 cho development. Để production, chuyển sang PostgreSQL
2. **Static files**: Chạy `python manage.py collectstatic` trước deploy
3. **Secret Key**: Generate key bảo mật mới trước production
4. **Debug Mode**: Tắt DEBUG=False trước deploy
5. **Environment**: Sử dụng `.env` file cho sensitive data

## 🚀 Production deployment

1. Sử dụng Gunicorn, uWSGI hoặc Waitress
2. Config Nginx/Apache as reverse proxy
3. Setup SSL/HTTPS
4. Config PostgreSQL database
5. Tối ưu static files caching
6. Setup monitoring & logging

## 📞 Support

- Admin Panel: http://127.0.0.1:8000/admin/
- Documentation: Full code comments included
- Templates: Responsive & well-structured
- Database: Properly indexed models

## 📅 Version Information

- **Django**: 4.2.7
- **Python**: 3.12.1
- **Bootstrap**: 5.1.3
- **Last Updated**: 2024

## 🎓 Học tập và phát triển

Website này được thiết kế để học tập về:
- Django ORM & Models
- Class-based & Function-based Views
- Template rendering & Inheritance
- Form handling & Validation
- Admin customization
- Front-end to Backend integration
- Authentication & Permissions
- CSS animations & Dark themes
- Responsive design

## 📝 License

PhoneShop - All rights reserved

---

**Happy Shopping! 🛍️**

Để bất kỳ câu hỏi nào, vui lòng kiểm tra Admin Panel hoặc Django documentation.
