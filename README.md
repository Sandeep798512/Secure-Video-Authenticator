# Secure Video Authenticator

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Django](https://img.shields.io/badge/Django-5.0%2B-green)
![Security](https://img.shields.io/badge/Security-SHA256%20%7C%20MD5-orange)

An end-to-end web platform designed for video media authentication, integrity verification, and tamper detection. Powered by **Python & Django (MVT Architecture)**, featuring cryptographic binary hashing, container signature inspection, interactive confidence scoring, and a modern dark glassmorphism dashboard.

---

## 🌟 Key Features

- 🛡️ **Cryptographic Fingerprinting**: Computes **SHA-256** and **MD5** binary checksums for every uploaded video file to detect unauthorized modifications.
- 🔍 **Header Magic Byte Inspection**: Analyzes binary file headers for valid container format magic signatures (`MP4`, `MKV`, `AVI`, `WebM`, `MOV`, `FLV`).
- 📊 **Authenticity Confidence Rating (0 - 100%)**: Dynamically computes an integrity rating for uploaded media with visual color-coded progress bars.
- 📜 **Detailed Forensic Audit Reports**: Dedicated audit certificate views displaying file size, upload metadata, SHA-256 fingerprinting, container type, and verification logs.
- 🔎 **Search & Filter Dashboard**: Filter media gallery by verification status (*Verified Authentic*, *Suspicious/Tampered*, *Warnings/Pending*) or keyword search.
- 🔐 **User Access Control**: Authentication system featuring account registration, secure login, user-bound media uploads, and permission-restricted video management.
- 🎨 **Responsive Dark Glassmorphism UI**: Built with Bootstrap 5, Bootstrap Icons, and clean CSS styling.

---

## 📁 Professional Directory Architecture

```
Secure-Video-Authenticator-main/
├── .vscode/
│   └── launch.json            # VS Code F5 Debugging configuration
├── media/                     # User-uploaded video storage
│   └── videos/
├── templates/                 # Global HTML templates
│   ├── base.html              # Layout shell with glassmorphism navigation & alerts
│   ├── login.html             # User login page
│   ├── signup.html            # User account registration page
│   └── videos/
│       ├── video_list.html    # Dashboard gallery & stats counter
│       ├── video_upload.html  # Secure video upload portal
│       └── video_detail.html  # Forensic audit certificate report
├── videoauth/                 # Core Django project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py            # Main settings (Media, Static, Auth)
│   ├── urls.py                # Main URL router
│   └── wsgi.py
├── videos/                    # Django Application module
│   ├── admin.py               # Django Admin registration
│   ├── apps.py
│   ├── forms.py               # SignUpForm & VideoForm definitions
│   ├── models.py              # Video entity model with forensic fields
│   ├── urls.py                # Video app URL patterns
│   ├── utils.py               # Cryptographic forensic verification engine
│   └── views.py               # View controllers & dashboard statistics
├── .gitignore                 # Version control ignore rules
├── db.sqlite3                 # Local SQLite database
├── manage.py                  # Django CLI management entry point
├── README.md                  # Project documentation
├── requirements.txt           # Dependency requirements
└── run.bat                    # Windows batch launcher script
```

---

## ⚡ Quick Start & Execution Guide

### Prerequisites
- Python 3.10+ installed on system.
- Django 5.0+ (`pip install -r requirements.txt`).

### Running in Visual Studio Code (VS Code)

#### Option 1: Press `F5` (Recommended)
1. Open the project folder in VS Code:
   `C:\Users\Er. SANDEEP GAUD\Desktop\Secure-Video-Authenticator-main`
2. Press **`F5`** on your keyboard.
3. Open your browser and navigate to **`http://127.0.0.1:8000/`**.

#### Option 2: VS Code Integrated Terminal
```cmd
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 8000
```
Open **`http://127.0.0.1:8000/`** in your browser.

#### Option 3: Double-Click `run.bat`
Double-click `run.bat` in the project root directory to automatically migrate database tables and launch the local development server.

---

## 🔐 Creating an Admin Account
To access the Django Administration interface (`http://127.0.0.1:8000/admin/`):
```cmd
python manage.py createsuperuser
```
Follow the prompts to enter your username, email, and admin password.

---

## 📄 License
This project is released under the MIT License.
