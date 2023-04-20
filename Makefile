all: pack

pack:
	pipreqs ./src --force


db-create:
	set PGPASSWORD=$(PWD)&&psql -h localhost -U postgres -c "create database \"TransBase\";"

db-drop:
	set PGPASSWORD=$(PWD)&&psql -h localhost -U postgres -c "DROP database \"TransBase\";"

db-init:
	@echo data base init
	rem rmdir /q /s "./src/migrations"
	cd ./src && flask db init

db-migrate:
	@echo database migration
	cd ./src && flask db migrate -m $(MSG)
	cd ./src && flask db upgrade

db-reconstruct: db-create db-init db-migrate