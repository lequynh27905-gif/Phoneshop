# Commands.md - Các Lệnh Django Thường Dùng

## Database & Migrations

```bash
# Tạo migrations mới từ models
python manage.py makemigrations

# Áp dụng migrations
python manage.py migrate

# Xem trạng thái migrations
python manage.py showmigrations

# Hoàn tác migration
python manage.py migrate store 0001  # Quay lại migration 0001
```

## Admin & Users

```bash
# Tạo tài khoản superuser (admin)
python manage.py createsuperuser

# Đổi mật khẩu user
python manage.py changepassword username

# Tạo tài khoản user thường
python manage.py shell
$ from django.contrib.auth.models import User
$ User.objects.create_user('username', 'email@example.com', 'password')
$ exit()
```

## Static Files & Media

```bash
# Thu thập static files
python manage.py collectstatic

# Xóa static files cũ trước khi thu thập lại
python manage.py collectstatic --clear

# Tìm static files
python manage.py findstatic file.css
```

## Development Server

```bash
# Chạy development server
python manage.py runserver

# Chạy trên port khác
python manage.py runserver 0.0.0.0:8001

# Reload tự động khi có thay đổi
python manage.py runserver --reload
```

## Database Management

```bash
# Dumping data từ database
python manage.py dumpdata > data.json

# Load data vào database
python manage.py loaddata data.json

# Xóa tất cả dữ liệu (cổng)
python manage.py flush
```

## Django Shell

```bash
# Mở Django shell
python manage.py shell

# Trong shell:
from store.models import Phone, Category, Order
phones = Phone.objects.all()
phones.count()
phone = phones.first()
print(phone.name, phone.price)

# Tạo danh mục mới
Category.objects.create(name='iPhone', slug='iphone')

# Cập nhật
phone = Phone.objects.get(id=1)
phone.price = 10000000
phone.save()

# Xóa
phone.delete()

# Filter
expensive_phones = Phone.objects.filter(price__gte=20000000)
iphones = Phone.objects.filter(brand='Apple')
```

## Testing

```bash
# Chạy tất cả tests
python manage.py test

# Chạy tests của app cụ thể
python manage.py test store

# Chạy test cụ thể
python manage.py test store.tests.TestPhoneModel

# Verbose output
python manage.py test -v 2
```

## Lint & Format

```bash
# Check code style
python manage.py check

# Format code (cần install black)
black .

# Lint (cần install flake8)
flake8

# Kiểm tra import
python -m isort .
```

## Production Deployment

```bash
# Tạo secret key mới
python manage.py shell
$ from django.core.management.utils import get_random_secret_key
$ print(get_random_secret_key())

# Chạy tất cả checks
python manage.py check --deploy

# Collect static files cho production
python manage.py collectstatic --noinput
```

## Utilities

```bash
# Xem tất cả URLs
python manage.py show_urls

# Xem database schema
python manage.py sqlmigrate store 0001

# Xem SQL query của migrations
python manage.py sqlsequencereset store

# Xem các ứng dụng đã cài
python manage.py showcapabilities

# Tạo extension PostgreSQL
python manage.py dbshell
```

## Useful Tips

```bash
# Xem environment variables
python manage.py shell -c "import os; print(os.environ)"

# Restart development server
# Ctrl + C để dừng, rồi chạy lại python manage.py runserver

# Clear all caches
python manage.py shell
$ from django.core.cache import cache
$ cache.clear()

# Xem size database
python manage.py dbshell
sqlite> .dbinfo
```
