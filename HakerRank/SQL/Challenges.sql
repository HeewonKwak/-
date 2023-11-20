-- Basic Join / Challenges
-- https://www.hackerrank.com/challenges/challenges/problem?isFullScreen=true
/*
Enter your query here.
*/
SET sql_mode = "";
WITH max_cnt AS (
    SELECT
        hacker_id,
        COUNT(challenge_id) AS cnt
    FROM Challenges
    GROUP BY hacker_id
)

SELECT
    h.hacker_id,
    h.name,
    c.cnt
FROM
    Hackers h
LEFT JOIN
    max_cnt c ON h.hacker_id = c.hacker_id
WHERE
    h.hacker_id IN (
        SELECT
            hacker_id
        FROM
            max_cnt
        WHERE
            cnt = (SELECT MAX(cnt) FROM max_cnt)
    ) 
    OR
    h.hacker_id IN (
        SELECT
            hacker_id
        FROM
            max_cnt
        GROUP BY
            cnt
        HAVING
            COUNT(cnt) = 1
    )
ORDER BY
    c.cnt DESC, h.hacker_id;
