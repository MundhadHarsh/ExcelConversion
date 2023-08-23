REM cd D:\RCOEM\Excel Project\excelproject
REM python manage.py runserver
REM start "chrome.exe" http://127.0.0.1:8000/

@echo off
start "Django Development Server" cmd /c "python manage.py runserver & start http://127.0.0.1:8000"

start chrome http://127.0.0.1:8000