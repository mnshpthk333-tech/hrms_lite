# HRMS Lite – Full-Stack Coding Assignment

## Project Overview
HRMS Lite is a lightweight Human Resource Management System designed for small-scale internal HR operations.  
This web-based application allows an admin to:

- Manage employee records (add, view, delete)
- Track daily attendance (mark present/absent, view attendance history)

The goal is to provide a simple, usable, and professional interface for essential HR tasks, focusing on clean, stable, and functional features.

---

## Tech Stack

- **Backend:** Python, Django, Django Rest Framework (DRF)
- **Frontend:** HTML, CSS, DTL
- **Database:** SQLite 
- **Development Tools:** VS Code, Python 
- **Version Control:** Git 



## Features

### Employee Management
- Add new employees with:
  - Employee ID (unique)
  - Full Name
  - Email Address
  - Department
- View a list of all employees
- Delete an employee

### Attendance Management
- Mark attendance for an employee with:
  - Date
  - Status (Present / Absent)
- View attendance records for each employee

---

## Getting Started (Run Locally)

### Prerequisites
- Python 3.8+ installed
- VS Code (or preferred IDE)
- `pip` for Python package management

### Steps

1. **Clone the repository**
```bash
git clone <repository-url>
cd hrms-lite
