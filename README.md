# EduTrack – Student & Course Management System

EduTrack is a modern, full-stack student management system built with Django. It provides a comprehensive dashboard for administrators to manage students, courses, and enrollments with a clean and intuitive interface.

## 🚀 Features

-   **Dashboard:** real-time statistics on students, courses, and enrollments.
-   **Student Management:** Complete CRUD operations for students, including search and profile details.
-   **Course Management:** Manage course offerings, descriptions, and credit allocations.
-   **Enrollment System:** Easily enroll students in courses with status tracking (Enrolled, Completed, Dropped).
-   **Secure Authentication:** User registration and login system with persistent profiles.
-   **Modern UI:** Styled with the Studio Chalk design system for a premium aesthetic.

## 🛠 Tech Stack

-   **Backend:** Python 3.12+, Django 5.x
-   **Frontend:** HTML5, CSS3, Vanilla JavaScript (Studio Chalk Theme)
-   **Database:** SQLite (default for development)
-   **Package Manager:** [uv](https://github.com/astral-sh/uv)

## 📂 Project Structure

```text
EduTrack/
├── apps/               # Django Applications
│   ├── accounts/       # User profiles and authentication
│   ├── courses/        # Course management
│   ├── dashboard/      # Main admin dashboard
│   ├── enrollments/    # Student course enrollments
│   └── students/       # Student records
├── static/             # Global static assets (CSS, JS)
├── templates/          # Global HTML templates
├── docs/               # Project documentation
│   ├── to_start/       # Pending features/tasks
│   └── completed/      # Finished feature documentation
├── edutrack/           # Project configuration
├── pyproject.toml      # Dependency management
└── README.md           # Project overview
```

## 🏁 Getting Started

### Prerequisites
- Install **uv**: `curl -LsSf https://astral-sh.uv.run/install.sh | sh`

### Installation
1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd EduTrack
    ```
2.  **Sync dependencies:**
    ```bash
    uv sync
    ```
3.  **Activate virtual environment:**
    ```bash
    source .venv/bin/activate
    ```
4.  **Run migrations:**
    ```bash
    python manage.py migrate
    ```
5.  **Start development server:**
    ```bash
    python manage.py runserver
    ```
    The app will be available at `http://127.0.0.1:8000/`.

## 🧪 Testing
Run the automated test suite:
```bash
python manage.py test
```

## 🏗 Architecture & Coding Standards

To maintain a high-quality codebase, EduTrack follows these standards:

### Coding Standards
- **Django Best Practices:** Use Class-Based Views (CBVs) for standard CRUD operations to keep logic concise and reusable.
- **Clean Routing:** URL patterns are namespaced and separated by application.
- **Documentation:** Every major feature includes a documentation update in the `docs/` directory.
- **Code Style:** Follow PEP 8 guidelines for Python code and maintain meaningful variable/function naming.
- **Comments:** Add descriptive comments for complex logic or business rules.

### Design System
- **Studio Chalk:** All UI components must adhere to the Studio Chalk design system, focusing on high-contrast, accessible, and premium interfaces.

## 📄 Documentation

Detailed implementation steps and architectural decisions can be found in the `docs/` directory:
- [To-Start (Pending)](file:///Users/anju/EduTrack/docs/to_start/)
- [Completed](file:///Users/anju/EduTrack/docs/completed/)
