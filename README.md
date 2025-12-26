# Study Calendar

A Flask-based web application for managing study plans and tracking learning progress.

## Features

- Annual learning calendar with 12-month view
- Study plan management
- Color-coded plans for easy visualization
- Progress tracking (completed, partial, missed)
- Template system for reusable study content
- User authentication

## Tech Stack

- Backend: Flask, SQLAlchemy
- Database: MS SQL Server
- Frontend: Tailwind CSS, JavaScript
- Python 3.14+

## Installation

1. Clone repository
```bash
git clone https://github.com/pinkyj81/study_plan.git
cd study_plan
```

2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure database in `db_config.py`

5. Run application
```bash
python app.py
```

6. Access at http://localhost:5000

## Project Structure

```
study_calendar/
├── app.py
├── db_config.py
├── models.py
├── create_tables.py
├── seeds.py
├── requirements.txt
├── static/
└── templates/
    ├── index.html
    ├── login.html
    └── template_manage.html
```

## Usage

1. Login with username (auto-creates account)
2. Create study plan with "New Plan" button
3. Click calendar dates to add study content
4. Track progress with status updates
5. Customize plan colors

## License

MIT License

## Developer

pinkyj81
