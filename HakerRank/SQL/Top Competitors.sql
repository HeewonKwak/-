-- Basic Join / Top Competitors
-- https://www.hackerrank.com/challenges/full-score/problem?isFullScreen=true

/*
Enter your query here.
*/
SELECT
t.hd,
t.ne
FROM (
    SELECT
    h.hacker_id AS hd,
    h.name AS ne,
    COUNT(s.submission_id) AS cnt
    FROM Hackers h
    INNER JOIN Submissions s
    ON (h.hacker_id = s.hacker_id)
    INNER JOIN Challenges c
    ON (c.challenge_id = s.challenge_id)
    INNER JOIN Difficulty d
    ON (c.difficulty_level   = d.difficulty_level)
    WHERE d.score = s.score
    GROUP BY h.hacker_id, h.name
) AS t
WHERE t.cnt > 1
ORDER BY t.cnt DESC, t.hd