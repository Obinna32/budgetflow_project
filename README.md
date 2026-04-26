# 📈 BudgetFlow - Personal Finance Tracker

BudgetFlow is a clean, functional fullstack web application built with **Django** to help users track their income and expense. It features a personalizd dashboard, secure authentication, and real-time financial summaries.

##  🚀 Features
- **User Authentication:** Secure signup and login system. Every user manages their own private financial data.
- **Transaction Management (CRUD):** Full capability to Create, Read, Update and Delete income and expense records.
- **Financial Dashboard:** A summary section that automatically calculates:
    - **Total Income**
    - **Total Expenses**
    - **Net Balance**
- **Search & Filtering:** Users can search for specific transactions by title or filter by category.
- **Smart UI Notification:** Built-in success message - after deleting a record that automatically disappear after 3 seconds for a smooth user experience.
- **Responsive Styling:** Custom CSS designed for a professional modern look.

## 🛠️ Tech Stack
- **Backend:** Python 3.13+, Django 6.0+
- **Frontend:** HTML5, CSS3, JavaScript (for UI timeouts)
- **Database:** SQLite (default Django DB)
- **Version Control:** Git, GitHub

## 📦 Installation & Setup

1. **Clone the repository:**
```bash
git clone https://github.com/Obinna32/budgetflow_project.git
cd budgetflow_project
```
2. **Set up a virtual environment:**
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

3. **Install all requirements:**
In your terminal, run this
```bash
pip install -r requirements.txt
```

4. **Final Run:**
In your terminal, run
```
python manage.py runserver
```