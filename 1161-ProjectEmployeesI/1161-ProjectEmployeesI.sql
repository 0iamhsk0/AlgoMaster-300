-- Last updated: 10/7/2025, 6:52:20 PM
SELECT 
  p.project_id, 
  ROUND(AVG(e.experience_years), 2)::NUMERIC AS average_years
FROM Project p
INNER JOIN Employee e
USING (employee_id)
GROUP BY p.project_id;
