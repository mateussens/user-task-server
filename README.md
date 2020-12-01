# User-task

## Introduction

These project represents an api that is used to list users and user's task. Technical test for Smarket, by Mateus Sens.

I used python 3.8 and DjangoRestFramework to build this API.

technical debt:
- Authentication

## Dependencies

All dependencies and your versions is in [requirements.txt [click here]](https://github.com/mateussens/user-task-server/blob/master/requirements.txt)

## Contributors

* [Mateus Sens](mateussens@gmail.com)


### Running with Docker

* Install Docker and Docker Compose 1.27.4

1) To run the server
```
$ make build-database password=postgres (use your local postgres password "postgres" is deafult)
$ make up
```
After the command '$ make up' you can access http://localhost:8000


### Api documentation
```
http://0.0.0.0:8000/doc/
```

### Running Tests

```
$ make unittests
```

### List of commands:

|  Shortcut |   |  Command (For windows or without make) |   |  Description |
|---|---|---|---|---|
| ``` $ make build ```  |   | 	docker build -t user-api .  |   | Building local image for user container  |
| ``` $ make build-database ```  |   | docker-compose up -d user-api && docker exec -it user-api psql -h localhost -U postgres -c "CREATE DATABASE user_db WITH OWNER = postgres ENCODING = 'UTF8' TABLESPACE = pg_default LC_COLLATE = 'en_US.utf8' LC_CTYPE = 'en_US.utf8' CONNECTION LIMIT = -1;"  |   |  To build locally database user_db  |
| ``` $ make up ```  |   | 	docker-compose up user-api  |   |  Running builded image locally. After this you can access "http://localhost:8000" |
| ``` $ make rm-all ```   |   |  	docker rm -f user-api && 	docker rm -f user-database |   |  Removing all started containers |
| ``` $ make code-convention ```  |   |  	docker-compose up -d user-api && docker exec -it user-api flake8 /webapps |   | Run Code Style with flake in our project.  |
| ``` $ make unittests ```  |   |  	docker-compose run user-unittests |   | To Run Tests  |
