password?=postgres

up: build
	docker-compose up $(dettach) user-api
build:
	docker build -t user-api .
unittests:
	docker build -t user-unittests .
	docker-compose run user-unittests
code-convention: build
	docker-compose up -d user-api
	docker exec -it user-api flake8 /webapps
	make rm-all
rm-all:
	docker rm -f user-api
	docker rm -f user-database
build-database: build
	docker-compose up -d user-api
	docker exec -it -e PGPASSWORD=$(password) user-api psql -h localhost -U postgres -c "CREATE DATABASE user_db WITH OWNER = postgres ENCODING = 'UTF8' TABLESPACE = pg_default LC_COLLATE = 'en_US.utf8' LC_CTYPE = 'en_US.utf8' CONNECTION LIMIT = -1;"
