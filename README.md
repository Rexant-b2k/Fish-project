# Fish-project [backend] ver 0.1a
## _Educational quizzle game_
## based on:
[![N|Solid](https://static.djangoproject.com/img/logos/django-logo-negative.svg)](https://www.djangoproject.com/)
## and
[![N|Solid](https://www.django-rest-framework.org/img/logo.png)](https://www.django-rest-framework.org/)
## and also on:
[![N|Solid](https://cdn.icon-icons.com/icons2/2699/PNG/512/gunicorn_logo_icon_170045.png)](https://gunicorn.org/)

Fish-project is a hobby project for entertainment, learning, testing and improving skills on python and frameworks/


## Features
This module is a part of whole Fish project, contains only backend API module, which could be connected using json exchange of data plus admin module.

- Could create questions, quizzles, image-questions
- There is generator of random tasks
- Solved tasks are not repeating until player resets his progress
- Coould score point for each correct answer and store it for every player.
- Could use SSL technology (https connection) to be safe backend part for modern instant messaging services (Telegram, Whatsap)

## Tech

Fish project uses a number of open source projects to work properly:

- [Python] - Python 3.10
- [Django] - Web framework to rule them all!
- [Django Rest Framework (DRF)] - REST API support for Django
- [Gunicorn] - WSGI server to use Django in high worload scenarios


And of course Fish-project itself is open source with a [public repository][Rexant-b2k]
 on GitHub.

## Installation


Install the dependencies and devDependencies and start the server (Linux/MacOS example).

```sh
cd yatube
python3 -m pip install --upgrade pip
python3 -m venv venv
source venv/bin/activate
```

For production environments (automatic)...

```sh
pip install -r requirements.txt
```


## Making migrations
```sh
venv..$ python manage.py migrate
```

## Running DEV server
```sh
venv..$ python manage.py runserver
```

##### Full information about possible request is available at **http://127.0.0.1:8000/redoc/ in your browser**

## Requests example
*Could be done using Postman or another simular app, or via browser.
###### Get random task(question):
Request:
```
http://localhost:8000/api/v1/randomtask/
```
Response:
```sh
[
    {
        "id": 0,
        "header": "string",
        "text": "string",
        "image": "http://example.com",
        "category": "string",
        "topic": "string",
        "add_date": "2019-08-24T14:15:22Z",
        "answer": "string"
    }
]
```
###### Update player info:
Request:
```
PATCH http://localhost:8000/api/v1/player/{id}/
```
```sh
{
    "player_id": "string",
    "score": 0,
    "solved_tasks": 
    [
        0
    ]
}
```

Response:
```sh
{
    "id": 0,
    "player_id": "string",
    "score": 0,
    "solved_tasks": 
    [
        0
    ]
}
```


## Plugins

Fish-project is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.

| Plugin    | README         |
| ----------| -------------- |
| Dillinger | [Dillinger.io] |

## Docker

The information will be available in future.

## Feature plans
1. Improve the technology of resetting results: cleaning score for the resseted groups of questions
2. Docker realization
3. Improve authentication (using token)
4. Keeping extended statistics on backend site
5. API v2 to comply with paragragh 2
6. Fix logo in readme
7. Create list of version improvements
8. Dual language version

## License

BSD-3 Clause License

**Free Software, Hello everybody**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [Rexant-b2k]: <https://github.com/Rexant-b2k>
   [git-repo-url]: <https://github.com/Rexant-b2k/Fish-project>
   [Django]: <https://www.djangoproject.com>
   [Python]: <https://www.python.org/>
   [Django Rest Framework (DRF)]: <https://www.django-rest-framework.org/>
   [Dillinger.io]: <https://dillinger.io/>
   [Gunicorn]: <https://gunicorn.org/>