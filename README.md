# Udemy Course Redirector

A minimal, fast, and SEO-friendly website to bridge Telegram course posts to Udemy. Built with FastAPI, SQLite (production-ready for small scale), and Jinja2 templates.

## specific Features
- **Zero Authentication**: Open API for automation scripts.
- **Fast & Minimal**: Server-side rendered HTML for max speed and SEO.
- **Dark Mode UI**: Clean, modern, mobile-first design.
- **Automated Slugs**: Titles are automatically converted to clean URLs.

## Project Structure
```
autoweb/
├── app/
│   ├── main.py        # Application entry point & API/Page logic
│   ├── models.py      # Database models (SQLAlchemy)
│   ├── schemas.py     # Pydantic schemas for validation
│   ├── crud.py        # Database operations
│   ├── database.py    # Database connection logic
│   ├── templates/     # HTML templates (Jinja2)
│   └── static/        # CSS & static assets
├── requirements.txt   # Python Dependencies
└── README.md          # Documentation
```

## Setup & Run

1. **Install Python 3.8+**
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Server**:
   ```bash
   uvicorn app.main:app --reload
   ```
   The app will start at `http://127.0.0.1:8000`.

## API Documentation
Interactive docs are available at: `http://127.0.0.1:8000/docs`

### Example: Post a New Course
Use this command to add a course via your automation script.

**Endpoint:** `POST /api/courses`

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/api/courses' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "Complete Python Bootcamp 2025",
  "description": "Learn Python from scratch to advanced in this comprehensive course. Includes 100+ exercises.",
  "duration": "22h 30m",
  "lectures": 150,
  "assignments": 25,
  "rating": 4.8,
  "instructor": "Jose Portilla",
  "udemy_link": "https://www.udemy.com/course/complete-python-bootcamp/",
  "tags": "Python, Programming, Backend"
}'
```

**Response:**
```json
{
  "title": "Complete Python Bootcamp 2025",
  "slug": "complete-python-bootcamp-2025",
  "id": 1,
  "created_at": "2025-12-31T10:00:00.000000"
}
```

## Deployment
This application is ready for deployment on platforms like Railway, Render, or Heroku.
- **Database**: Defaults to `sqlite:///./courses.db`. For production with MongoDB or PostgreSQL, update `app/database.py`.
- **Environment**: No strict ENV variables required for local run.
