#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== PhoneShop Django Setup ===${NC}\n"

# 1. Create virtual environment
echo -e "${GREEN}1. Tạo virtual environment...${NC}"
python -m venv venv

# 2. Activate virtual environment
echo -e "${GREEN}2. Kích hoạt virtual environment...${NC}"
source venv/bin/activate  # Trên macOS/Linux
# venv\Scripts\activate  # Trên Windows

# 3. Install requirements
echo -e "${GREEN}3. Cài đặt các gói phụ thuộc...${NC}"
pip install -r requirements.txt

# 4. Create .env file
echo -e "${GREEN}4. Tạo file .env...${NC}"
if [ ! -f .env ]; then
    cp .env.example .env
    echo "File .env đã được tạo. Vui lòng cập nhật SECRET_KEY"
fi

# 5. Run migrations
echo -e "${GREEN}5. Chạy migrations...${NC}"
python manage.py migrate

# 6. Create superuser
echo -e "${GREEN}6. Tạo tài khoản admin...${NC}"
python manage.py createsuperuser

# 7. Collect static files
echo -e "${GREEN}7. Thu thập static files...${NC}"
python manage.py collectstatic --noinput

echo -e "${GREEN}=== Setup hoàn thành! ===${NC}"
echo -e "${GREEN}Chạy server với lệnh: python manage.py runserver${NC}"
echo -e "${GREEN}Admin panel: http://127.0.0.1:8000/admin/${NC}"
