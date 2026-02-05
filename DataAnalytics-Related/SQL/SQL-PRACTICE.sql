SELECT * FROM Parks_and_Recreation.parks_departments;

# Joining multiple Tables 
SELECT * FROM employee_demographics as demo
INNER JOIN employee_salary as sal 
ON demo.employee_id = sal.employee_id
INNER JOIN parks_departments as pd 
ON sal.dept_id = pd.department_id;

# Unions - Unions allow you to combine rows together from separate or from same table

SELECT age, gender
FROM employee_demographics
UNION
SELECT first_name, last_name
FROM employee_salary;

 