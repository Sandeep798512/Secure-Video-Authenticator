@echo off
echo ========================================================
echo         SECURE VIDEO AUTHENTICATOR SERVER
echo ========================================================
cd /d "%~dp0"
echo Applying database migrations...
python manage.py makemigrations
python manage.py migrate
echo.
echo Launching Django server on http://127.0.0.1:8000/
echo Press Ctrl+C in this window to stop the server.
echo.
python manage.py runserver 8000
pause
