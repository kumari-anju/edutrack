


Create a full-stack web project named **EduTrack – Student & Course Management System** using the Django framework.

Tech stack:

* Backend: Python with Django
* Frontend: HTML, CSS, Bootstrap, JavaScript
* Database: SQLite (default Django database)
* Version Control Ready: Git/GitHub friendly

Project goals:
Build a simple system where an admin can manage students, courses, and enrollments. The application should support CRUD operations and a dashboard.

### Required Django Apps

Create the following apps inside the project:

1. **accounts**

   * authentication (login, logout)
   * user profile

2. **students**

   * add student
   * edit student
   * delete student
   * list students

3. **courses**

   * add course
   * update course
   * delete course
   * view courses

4. **enrollments**

   * assign students to courses
   * track enrollments

5. **dashboard**

   * show statistics
   * total students
   * total courses
   * total enrollments

### Basic Models

Create models for:

* Student
* Course
* Enrollment
* User Profile

Use proper Django relationships such as:

* ForeignKey
* OneToOneField

### Folder Structure

Create a clean and maintainable folder structure.

edutrack/
│
├── manage.py
├── requirements.txt
│
├── edutrack/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── apps/
│   ├── accounts/
│   ├── students/
│   ├── courses/
│   ├── enrollments/
│   └── dashboard/
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── students/
│   ├── courses/
│   └── enrollments/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/

### Documentation Requirement

Inside the root project folder create a **docs/** directory.

Inside docs create two folders:

docs/
│
├── start/
│
└── completed/

### Documentation Rules

1. All documentation files must use the **.md (Markdown)** extension.
2. The **start** folder will contain planning and design documentation before development begins.
3. The **completed** folder will contain final documentation after the project is finished.
4. Each document should follow clear headings and sections.

### Files inside docs/start/

Create the following markdown files:

docs/start/
│
├── project-overview.md
├── feature-list.md
├── system-architecture.md
├── database-design.md
├── api-plan.md
├── development-roadmap.md

### Files inside docs/completed/

Create the following markdown files:

docs/completed/
│
├── installation-guide.md
├── project-structure.md
├── database-schema.md
├── api-documentation.md
├── deployment-guide.md
├── user-manual.md

### Coding Standards

* Follow Django best practices
* Use class-based views when possible
* Separate business logic properly
* Use reusable templates
* Maintain clean URL routing

### Additional Instructions

* Add comments in the code where necessary
* Make the dashboard responsive using Bootstrap
* Ensure project is GitHub-ready
* Include requirements.txt
* Include README.md at root explaining the project

Output:

1. Full Django project structure
2. Sample models
3. Basic views
4. URL routing
5. Documentation folder structure
6. Initial markdown documentation templates
