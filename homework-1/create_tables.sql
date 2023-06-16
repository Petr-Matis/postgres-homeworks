-- SQL-команды для создания базы
CREATE DATABASE north;

-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	employees_id smallint PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	title varchar(100) NOT NULL,
	birth_date date,
	notes text
);

CREATE TABLE customers
(
	customer_id varchar(10) PRIMARY KEY,
	company_name varchar(100) NOT NULL,
	contact_name varchar(100) NOT NULL
);

CREATE TABLE orders
(
	order_id integer PRIMARY KEY,
	customer_id varchar(10) REFERENCES customers(customer_id) NOT NULL,
	employee_id integer REFERENCES employees(employees_id) NOT NULL,
	order_date date NOT NULL,
	ship_city varchar(100) NOT NULL
);