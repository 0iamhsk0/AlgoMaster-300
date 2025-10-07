-- Last updated: 10/7/2025, 6:51:59 PM
SELECT 
  contest_id, -- 1
  ROUND(COUNT(user_id) * 100.0 / (SELECT COUNT(*) FROM Users), 2) AS percentage -- 2
FROM Register
GROUP BY 1
ORDER BY 
  2 DESC,
  1 ASC;
