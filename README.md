# Smart-Campus-Helpdesk-API-Backend-Project-
A backend REST API for a Smart Campus Helpdesk system. Students can raise issues (tickets) and administrators can manage them. 
Project Overview
You are required to build a backend REST API for a Smart Campus Helpdesk system. Students
can raise issues (tickets) and administrators can manage them. This project must be implemented
using Django and Django REST Framework only.
Objective
The goal of this project is to apply all the backend concepts taught so far, including CRUD
operations, authentication, pagination, filtering, ordering, and API design. The project should be
structured in a clean and professional manner.
Core Features to Implement- Django project and app setup- PostgreSQL database integration- Ticket model with proper fields- CRUD APIs for tickets- JWT-based authentication- Admin login (session authentication)- Pagination for ticket listing- Filtering by category and status- Ordering by priority and created date- Search by title or description- Future-ready Redis caching (do not implement now)
Data Model (Ticket)
id (Auto Field)
title (CharField)
description (TextField)
category (CharField: classroom / hostel / network)
priority (CharField: low / medium / high)
status (CharField: open / in-progress / closed)
created_at (DateTimeField)
updated_at (DateTimeField)
Authentication Flow
1. User logs in using username and password.
2. JWT access and refresh tokens are generated.
3. Access token is sent in Authorization header for protected APIs.
4. Admin users can also access APIs via browser session login.
API Endpoints (Wireframe)
POST /api/token/ (Login)
POST /api/token/refresh/
POST /tickets/ (Create ticket)
GET /tickets/ (List tickets)
GET /tickets/<id>/ (Ticket details)
PATCH /tickets/<id>/ (Update status)
DELETE /tickets/<id>/ (Delete ticket)
Ticket Listing Flow
GET /tickets/
→ Apply filtering (category, status)
→ Apply ordering (priority, created_at)
→ Apply pagination (page size)
→ Return paginated response
Redis (Future Enhancement)
Redis should be used later to cache the ticket list API.
Cache must be cleared when tickets are created, updated, or deleted.
No Redis implementation is required at this stage.
Submission Guidelines- Submit the complete Django project folder.- PostgreSQL must be used as the database.- Code should be properly formatted and commented.- APIs must be tested using Postman.- Screenshots of API responses should be included.
Evaluation Criteria- Correct API functionality- Proper use of authentication and permissions- Clean project structure- Correct use of pagination and filtering- Code readability and clarit
