-- Basic Join / Ollivander's Inventory
-- https://www.hackerrank.com/challenges/harry-potter-and-wands/problem?isFullScreen=true
/*
Enter your query here.
*/
SELECT
t2.id,
t1.age,
t1.coins_needed,
t1.power
FROM (
    SELECT
    ttt.age,
    MIN(ttt.coins_needed) AS coins_needed,
    ttt.power
    FROM (
    SELECT
    w.id AS id,
    wp.age AS age,
    w.coins_needed AS coins_needed,
    w.power AS power
    FROM Wands w
    LEFT JOIN Wands_Property wp
    ON w.code = wp.code
    WHERE wp.is_evil = 0
) ttt
    GROUP BY ttt.age, ttt.power
) t1
LEFT JOIN (
    SELECT
    w.id AS id,
    wp.age AS age,
    w.coins_needed AS coins_needed,
    w.power AS power
    FROM Wands w
    LEFT JOIN Wands_Property wp
    ON w.code = wp.code
    WHERE wp.is_evil = 0
) t2
ON t1.age = t2.age and t1.power = t2.power and t1.coins_needed = t2.coins_needed
ORDER BY 4 DESC, 2 DESC