A simple RESTful API built with Django and Django REST Framework that allows users to register, log in, and manage their daily tasks. This project is beginner-friendly and follows token-based authentication for protected endpoints.


🚀 Features
✅ User Registration & Login

🔐 Token-based Authentication (TokenAuth)

📋 Create, Read, Update & Delete (CRUD) Tasks

👤 Each task is tied to an authenticated user

📂 Filter tasks by status (optional if implemented)

🧩 Organized with proper Django app/project structure

📖 Interactive API docs with Swagger UI (if enabled)

🧪 Postman Collection for testing endpoints


📁 Endpoints
Method	Endpoint	Description
POST	/api/register/	Create a new user
POST	/api-token-auth/	Login & get token	
GET	/api/tasks/	List all tasks (user only)	
POST	/api/tasks/	Create a new task	
GET	/api/tasks/<id>/	Retrieve a single task
PUT	/api/tasks/<id>/	Update a task	
DELETE	/api/tasks/<id>/	Delete a task


postman documentation link: https://documenter.getpostman.com/view/43781426/2sB34oDdgj

🧪 Live API Demo
📌 Coming Soon: Public Postman Documentation with real-time testing