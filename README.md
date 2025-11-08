# 🗂️ Django To-Do Manager

A **clean and modern To-Do List web application** built with **Django**, designed to help users manage daily tasks efficiently.  
Includes user authentication, CRUD operations, and a responsive UI — perfect for learning Django through a real-world project.

---

## 🚀 Features

- ✨ User registration, login & logout  
- ✅ Create, edit, delete, and mark tasks as complete  
- 👤 Each user has their own private task list  
- 🔍 Search and filter tasks easily  
- 💾 Powered by Django ORM and SQLite  
- 🎨 Responsive design with Bootstrap  

---

## 🧠 Tech Stack

| Layer | Technology |
|-------|-------------|
| Backend | Python, Django |
| Frontend | HTML, CSS, Bootstrap |
| Database | SQLite (default) |
| Version Control | Git & GitHub |

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally 👇

```bash
# 1️⃣ Clone the repository
git clone https://github.com/yourusername/django-todo-manager.git

# 2️⃣ Navigate to the project folder
cd django-todo-manager

# 3️⃣ Create a virtual environment
python -m venv venv

# 4️⃣ Activate the environment
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# 5️⃣ Install dependencies
pip install -r requirements.txt

# 6️⃣ Run migrations
python manage.py migrate

# 7️⃣ Start the server
python manage.py runserver
