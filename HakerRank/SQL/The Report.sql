-- Basic Join / The Report
-- https://www.hackerrank.com/challenges/the-report/problem?isFullScreen=true

/*
Enter your query here.
*/
SELECT
CASE WHEN g.Grade >=8 THEN s.Name ELSE NULL END AS name,
g.Grade AS grade,
s.Marks AS marks
FROM Students s
LEFT JOIN Grades g
ON (s.Marks >= g.Min_Mark AND s.Marks <= g.Max_Mark)
ORDER BY g.Grade DESC, s.Name ASC, s.Marks ASC