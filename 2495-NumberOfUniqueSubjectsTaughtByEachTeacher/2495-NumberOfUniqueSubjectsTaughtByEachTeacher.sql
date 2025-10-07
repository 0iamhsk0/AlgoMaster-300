-- Last updated: 10/7/2025, 6:51:48 PM
-- Write your PostgreSQL query statement below
SELECT 
    teacher_id, COUNT(DISTINCT subject_id) AS cnt
FROM 
    Teacher 
GROUP BY
    1;