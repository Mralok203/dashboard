# dashboard
A full-stack web application for managing user registrations and purchase history, with a beautiful e-commerce-style dashboard. Built using Flask (Python) for the backend and HTML + Tailwind CSS for the frontend.

# 🛍️ LightHouse E-commerce User Management Portal

LightHouse is a lightweight e-commerce-style user management portal built using **Python Flask**, **HTML**, **TailwindCSS**, and **Pandas**, with data stored in an Excel file (`users.xlsx`). It supports individual user dashboards, admin overview, and item tracking.

## ✨ Features

### 🧑 User Functionality
- Register with: Name, Phone, Password, Email, Address, and Item
- Phone number uniqueness enforced
- Login using phone and password
- Dashboard shows **only their personal records** in tabular format
- Option to **add new purchase** (pre-filled form, only item is editable)

### 👑 Admin Functionality
- Admin login with fixed credentials: `admin` / `admin123`
- View all user data in a filterable table
- Filter by name or date

### 🎨 UI Highlights
- Elegant homepage styled like a modern e-commerce site
- Navbar includes Home, Login, and Register on all pages

## 📂 Project Structure

```
/
├── app.py                  # Flask backend
├── users.xlsx              # Data file for user records
├── templates/
│   ├── home.html           # Landing page
│   ├── login.html          # Login page (user + admin)
│   ├── register.html       # User registration page
│   ├── dashboard.html      # Dashboard for both users and admin
│   └── add_item.html       # Page to add item after login
└── static/                 # Optional folder for CSS or assets (not required with Tailwind CDN)
```

## 🛠️ How to Run Locally

1. **Install Python packages**:
```bash
pip install flask pandas openpyxl
```

2. **Run the application**:
```bash
python app.py
```

3. Visit: `http://127.0.0.1:5000/`

---

## 🔐 Admin Credentials

- **Username**: `admin`
- **Password**: `admin123`

---

## 🚀 Deployment

You can host this on free services like:
- [Render](https://render.com/)
- [Replit](https://replit.com/)
- [PythonAnywhere](https://www.pythonanywhere.com/)
- [Glitch](https://glitch.com/)

Make sure to allow read/write access to `users.xlsx` if using hosted environments.

---

## 📬 Contact

Created for demo and educational use by `mr.dash`.
