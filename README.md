
# ATM API Service

### An API service with two main endpoints, one for creating ATM devices and one for fetching all the devices.

## Installing the Database

- Install PostgreSQL and PostGIS on your system. (Google it base on your OS)

- Open a terminal and enter to the psql command environment

`psql -d postgres`
 
`CREATE DATABASE atm_service_db;`

`CREATE USER atm_service_user WITH PASSWORD '<YOUR_PASSWORD>';`

`ALTER ROLE atm_service_user SET client_encoding TO 'utf8';`

`ALTER ROLE atm_service_user SET default_transaction_isolation TO 'read committed';`

`ALTER ROLE atm_service_user SET timezone TO 'UTC';`

`GRANT ALL PRIVILEGES ON DATABASE atm_service_db TO atm_service_user;`


- Then install PostGIS extension on the created Database

`CREATE EXTENSION postgis;`

- Sometimes you need to change the owner of postgis table to your user

`ALTER TABLE spatial_ref_sys OWNER TO atm_service_user;`

## Creating .env file

- Copy .env.sample file and rename it to .env
- Replace the variables with your settings

## For creating tables in the Database

`flask db upgrade`

## Create a virtual environment and activate it

`python3 -m venv .venv`

## for installing dependencies

`pip install --upgrade pip`
`pip install -r requirements.txt`

## For running the server in dev environment

`flask run`

## For running with gunicorn

`gunicorn --bind 0.0.0.0:5000 wsgi:app`

You can use systemd to serve the wsgi file of this service in any server (Linux).

## TODO:
- Containerize the service
- Decouple database from main service
- Using RDS for Database
- Authentication/Authorization
- Using EC2 or (AWS API gateway and AWS lambda) to serve the API

## Test data for POST

{
  "address": "5426 HelloWorld Rd.",
  "provider": "WHO ATM",
  "geometry": {
    "type": "POINT",
    "coordinates": [-123.0597096, 49.2931366]
  }
}