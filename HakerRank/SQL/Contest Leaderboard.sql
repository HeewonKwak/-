-- Basic Join / Contest Leaderboard
-- https://www.hackerrank.com/challenges/contest-leaderboard/problem?isFullScreen=true

/*
Enter your query here.
*/
SELECT
h.hacker_id,
h.name,
SUM(s.score) AS ss
FROM Hackers h
INNER JOIN (
    SELECT
    hacker_id,
    challenge_id,
    MAX(score) AS score
    FROM Submissions
    GROUP BY hacker_id, challenge_id
) s
ON (h.hacker_id = s.hacker_id)
GROUP BY h.hacker_id, h.name having ss > 0
ORDER BY 3 DESC, 1