-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	first_name varchar(100),
	last_name varchar(100),
	birth_date date,
	notes text
);
CREATE TABLE customers
(
	customer_id varchar(20) PRIMARY KEY,
	company_name varchar(100),
	contact_name varchar(100)
);
CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id varchar(100) REFERENCES customers(customer_id),
	employee_id int,
	order_date date,
	ship_city varchar(100)

)
