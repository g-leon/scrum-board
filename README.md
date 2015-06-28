# scrum-board
A backend API built with Django/Tornado/Redis that can power a Scrum Board app

## Overview 
- The API is based on three elements: Sprints, Tasks and Users
- A task can belong to a sprint and can be assigned to a user
- A task that doesn't belong to a sprint is part of the backlog

## Dependecies
- PostgreSQL (default port)
- Redis (default port)

## Quick Start
```
- git clone git@github.com:g-leon/scrum-board.git
- cd scrum-board

Download dependecies
- pip install -r requirements.txt

Create an admin user
- python manage.py createsuperuser

Update database
- python manage.py migrate

Start app server
- python manage.py runserver

Start websocket server
- python websocket_server.py

Access api 
- http://localhost:8000/api/
```

## Examples
- `http://localhost:8000/api/tasks/?backlog=True` (returns all tasks that are not assigned to a sprint)
- `http://localhost:8000/api/tasks/?assigned=[USER_NAME]` (returns all tasks assigned to USER_NAME)
- `http://localhost:8000/api/sprints/?end_min=[DATE]` (returns all sprints ended after DATE) 

