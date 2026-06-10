# 🏛 ગુજરાતી સમાજ Community Management Portal

A complete, production-ready Django web application for Gujarati Samaj community management — with full Gujarati Unicode support, mobile-first design, and a custom admin dashboard.

---

## 📁 Project Structure

```
gujarati_samaj/
├── gujarati_samaj/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── families/                # Core: Families, Members, Contact
│   ├── models.py            # Family, Member, ContactInfo
│   ├── views.py             # Home, Directory, Detail, PDF
│   ├── urls.py
│   ├── admin.py
│   └── management/commands/
│       └── populate_sample_data.py
├── events/                  # Community Events
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── announcements/           # Community Announcements
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── gallery/                 # Photo Gallery with Lightbox
│   ├── models.py
│   ├── views.py
│   └── urls.py 
├── dashboard/               # Custom Admin Dashboard
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── accounts/                # Login / Auth
│   └── urls.py
├── templates/
│   ├── public/              # Public-facing pages
│   │   ├── base.html        # Navbar + Footer
│   │   ├── home.html
│   │   ├── family_directory.html
│   │   ├── family_detail.html
│   │   ├── family_pdf.html
│   │   ├── events.html
│   │   ├── event_detail.html
│   │   ├── announcements.html
│   │   ├── gallery.html
│   │   └── contact.html
│   └── admin_panel/         # Dashboard templates
│       ├── base.html
│       ├── login.html
│       ├── dashboard.html
│       ├── families.html
│       ├── family_form.html
│       ├── member_form.html
│       ├── event_form.html
│       └── announcement_form.html
├── static/                  # CSS, JS, Images
├── media/                   # Uploaded files
├── requirements.txt
└── manage.py
```

---

## 🎨 Design System

| Element      | Value                    |
|--------------|--------------------------|
| Primary Dark | `#0B1F4D` (Dark Blue)    |
| Accent       | `#FF8C00` (Saffron)      |
| Background   | `#FFFFFF` / `#F8F9FA`    |
| Font         | Poppins + Noto Sans Gujarati |

---

## 🚀 Step-by-Step Setup Guide

### 1. Prerequisites

```bash
# Python 3.10+ required
python --version

# PostgreSQL installed and running
psql --version
```

### 2. Create Virtual Environment

```bash
cd gujarati_samaj
python -m venv venv

# Activate
source venv/bin/activate          # Linux/Mac
venv\Scripts\activate             # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup PostgreSQL Database

```sql
-- Connect to PostgreSQL
psql -U postgres

-- Create database and user
CREATE DATABASE gujarati_samaj_db;
CREATE USER samaj_user WITH PASSWORD 'samaj_password_123';
ALTER ROLE samaj_user SET client_encoding TO 'utf8';
ALTER ROLE samaj_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE samaj_user SET timezone TO 'Asia/Kolkata';
GRANT ALL PRIVILEGES ON DATABASE gujarati_samaj_db TO samaj_user;
\q
```

> 💡 **Alternative:** For quick development, switch to SQLite in `settings.py` by commenting out the PostgreSQL block and uncommenting the SQLite block.

### 5. Configure Environment (Optional but Recommended)

```bash
# Create .env file
cat > .env << EOF
DB_NAME=gujarati_samaj_db
DB_USER=samaj_user
DB_PASSWORD=samaj_password_123
DB_HOST=localhost
DB_PORT=5432
EOF
```

### 6. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser (Admin Login)

```bash
python manage.py createsuperuser
# Enter: Username, Email, Password
```

### 8. Populate Sample Data

```bash
python manage.py populate_sample_data
```

### 9. Collect Static Files

```bash
python manage.py collectstatic
```

### 10. Run the Development Server

```bash
python manage.py runserver
```

---

## 🌐 URL Routes

| URL                          | Page                          | Access |
|------------------------------|-------------------------------|--------|
| `/`                          | Home Page                     | Public |
| `/vasti-patrak/`             | Family Directory              | Public |
| `/family/<id>/`              | Family Detail                 | Public |
| `/family/<id>/pdf/`          | Family PDF Export             | Public |
| `/events/`                   | Events List                   | Public |
| `/events/<id>/`              | Event Detail                  | Public |
| `/announcements/`            | Announcements                 | Public |
| `/gallery/`                  | Photo Gallery (with lightbox) | Public |
| `/contact/`                  | Contact Info                  | Public |
| `/accounts/login/`           | Admin Login                   | Public |
| `/dashboard/`                | Dashboard Home                | Staff  |
| `/dashboard/families/`       | Families List                 | Staff  |
| `/dashboard/families/add/`   | Add Family                    | Staff  |
| `/dashboard/events/add/`     | Add Event                     | Staff  |
| `/dashboard/announcements/add/` | Add Announcement           | Staff  |
| `/admin/`                    | Django Admin (full)           | Admin  |

---

## ✨ Features

### Public Website
- **Home** – Hero, stats, upcoming events, announcements, gallery preview
- **Vasti Patrak (Family Directory)** – Search by name, village, gotra, business. Paginated grid
- **Family Detail** – Full profile with members table, PDF download
- **Events** – Upcoming / Past tabs, event cards with date badge
- **Announcements** – Listed with date
- **Gallery** – Grid with lightbox image viewer, category filters
- **Contact** – Address, phone, email, social links

### Admin Dashboard
- Custom sidebar dashboard (separate from Django admin)
- Stats cards: Families, Members, Events, Announcements
- Line chart: Family registrations over 12 months
- Quick action buttons: Add Family, Event, Announcement, Gallery
- Family management with edit/view/add member/PDF actions
- Live search/filter on families table

### Technical Features
- ✅ Full Gujarati Unicode support (Noto Sans Gujarati font)
- ✅ Bootstrap 5 mobile-first responsive design
- ✅ Family PDF export (browser print-to-PDF)
- ✅ Image upload (family photo, member photo, events, gallery)
- ✅ Lightbox gallery viewer
- ✅ Django Admin customized with inline member editing
- ✅ Role-based access (staff-only dashboard)
- ✅ Pagination on family directory
- ✅ Family ID auto-generated (GSM-0001 format)
- ✅ Age auto-calculated from date of birth
- ✅ Chart.js analytics

---

## 👥 User Roles

| Role             | Access                                           |
|------------------|--------------------------------------------------|
| **Super Admin**  | Everything: Django admin + dashboard             |
| **Staff User**   | Dashboard: add/edit families, events, announcements |
| **Public**       | View website, search directory, download PDF     |

To make a user staff (dashboard access):
```bash
python manage.py shell
>>> from django.contrib.auth.models import User
>>> u = User.objects.get(username='your_username')
>>> u.is_staff = True
>>> u.save()
```

---

## 📝 Adding Gujarati Content

All models support full Gujarati Unicode text. Simply type or paste Gujarati in any field:

```
Name:     કનુભાઈ પટેલ
Village:  હિંમતનગર
Business: કૃષિ
```

The database stores UTF-8, the font (Noto Sans Gujarati) renders it beautifully.

---

## 🔧 Production Checklist

```python
# settings.py changes for production:
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
SECRET_KEY = 'your-real-secret-key-from-env'

# Use environment variables for DB credentials
# Set up Nginx + Gunicorn
# Configure SSL/HTTPS
# Run: python manage.py collectstatic
```

---

## 📦 Tech Stack

- **Backend:** Python 3.10+, Django 5.x
- **Database:** PostgreSQL (with SQLite option for dev)
- **Frontend:** Bootstrap 5.3, Vanilla JS
- **Charts:** Chart.js 4
- **Fonts:** Google Fonts (Poppins + Noto Sans Gujarati)
- **Icons:** Bootstrap Icons 1.11
- **Images:** Pillow (Django ImageField)

---

*Built with ❤️ for Gujarati Samaj community — ગુજરાતી સમાજ*
