-- Last updated: 10/7/2025, 6:52:15 PM
-- Write your PostgreSQL query statement below
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY author_id;