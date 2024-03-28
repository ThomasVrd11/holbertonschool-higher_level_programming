-- TASK : j'en peux plus
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
