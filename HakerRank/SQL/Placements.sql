-- Advanced Join / Placements
-- https://www.hackerrank.com/challenges/placements/problem?isFullScreen=true

/*
Enter your query here.
*/
SELECT
-- s.ID,
s.Name
-- p2.Salary,
-- f.Friend_ID,
-- p.Salary
FROM Students s
LEFT JOIN Friends f
ON (s.ID = f.ID)
LEFT JOIN packages p
ON (f.Friend_ID = p.ID)
LEFT JOIN packages p2
ON (s.ID = p2.ID)
WHERE p2.Salary < p.Salary
ORDER BY p.Salary