-- Last updated: 10/7/2025, 6:52:03 PM
SELECT COALESCE(EmployeeUNI.unique_id, NULL) AS unique_id, Employees.name
-- COALESCE is unnessary, since joins by default gives NULL for empty values
FROM Employees
LEFT JOIN EmployeeUNI ON Employees.id = EmployeeUNI.id;
