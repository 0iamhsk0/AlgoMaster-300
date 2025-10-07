-- Last updated: 10/7/2025, 6:51:56 PM
-- Write your PostgreSQL query statement below
SELECT tweet_id 
FROM Tweets
WHERE LENGTH(content) > 15;