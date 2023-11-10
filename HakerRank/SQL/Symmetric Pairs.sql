-- Advanced Join / Symmetric Pairs
-- https://www.hackerrank.com/challenges/symmetric-pairs/problem?isFullScreen=true
/*
Enter your query here.
*/
SELECT
f1.X,
f1.Y
FROM Functions f1
INNER JOIN Functions f2
ON (f1.Y = f2.X AND f1.X = f2.Y)
WHERE f1.X <= f1.Y
GROUP BY f1.X, f1.Y HAVING (f1.X = f1.Y AND COUNT(f1.Y) > 1) OR f1.X != f1.Y
ORDER BY f1.X