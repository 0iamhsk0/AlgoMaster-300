-- Last updated: 10/7/2025, 6:52:23 PM
-- Write your PostgreSQL query statement below
SELECT p.product_name, s.year, s.price
FROM Sales s
JOIN Product p 
USING(product_id) 