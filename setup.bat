@echo off
REM Colors for output
cls
echo.
echo ===== PhoneShop Django Setup =====
echo.

REM 1. Create virtual environment
echo 1. Creating virtual environment...
python -m venv venv

REM 2. Activate virtual environment
echo 2. Activating virtual environment...
call venv\Scripts\activate

REM 3. Install requirements
echo 3. Installing dependencies...
pip install -r requirements.txt

REM 4. Create .env file
echo 4. Creating .env file...
if not exist .env (
    copy .env.example .env
    echo .env file created. Please update SECRET_KEY
)

REM 5. Run migrations
echo 5. Running migrations...
python manage.py migrate

REM 6. Collect static files
echo 6. Collecting static files...
python manage.py collectstatic --noinput

echo.
echo ===== Setup completed! =====
echo Run server with: python manage.py runserver
echo Admin panel: http://127.0.0.1:8000/admin/
echo.
pause
