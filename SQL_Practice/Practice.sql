CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    salary INTEGER
);

INSERT INTO employees (name, salary)
VALUES
('Darshan', 50000),
('Rahul', 60000);

SELECT * FROM employees;
