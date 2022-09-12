
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