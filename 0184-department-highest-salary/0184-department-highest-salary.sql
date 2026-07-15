# Write your MySQL query statement below
SELECT Department.name AS Department,
       Employee.name AS Employee,
       Employee.salary AS Salary
FROM Employee
JOIN Department
  ON Employee.departmentId = Department.id
WHERE Employee.salary = (
    SELECT MAX(E2.salary)
    FROM Employee AS E2
    WHERE E2.departmentId = Employee.departmentId
);