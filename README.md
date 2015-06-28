# scrum-board
A backend API built with Django/Tornado/Redis that can power a Scrum Board app

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


