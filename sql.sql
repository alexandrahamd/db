CREATE TABLE employees (
	id_emp int PRIMARY KEY,
    first_name varchar(255),
    last_name varchar(255),
	decr varchar(255),
    birth_date date,
    notes varchar(255)
);

CREATE TABLE customers (
	customer_id varchar(255) PRIMARY KEY,
    company_name varchar(255),
    contact_name varchar(255)
);

CREATE TABLE orders (
	order_id int PRIMARY KEY,
	customer_id varchar(255) REFERENCES customers(customer_id),
	employee_id int REFERENCES employees(id_emp),
    order_date date,
    ship_city varchar(255)
);