-- Advanced Join / SQL Project Planning
-- https://www.hackerrank.com/challenges/sql-projects/problem?isFullScreen=true

/*
Enter your query here.
*/
SET @row1 := 0, @row2 := 0;

-- SELECT
-- @row1 := @row1 + 1 AS row_num,
-- p1.Start_Date AS Start_Date
-- FROM Projects p1
-- LEFT JOIN Projects p2
-- ON (p2.End_Date = p1.Start_Date)
-- WHERE p2.Start_Date IS NULL

SELECT
t1.Start_Date AS sd,
t2.End_Date AS ed
FROM
(SELECT
    @row1 := @row1 + 1 AS row_num,
    p1.Start_Date AS Start_Date
    FROM Projects p1
    LEFT JOIN Projects p2
    ON (p2.End_Date = p1.Start_Date)
    WHERE p2.Start_Date IS NULL) AS t1,
(SELECT
    @row2 := @row2 + 1 AS row_num,
    p1.End_Date AS End_Date
    FROM Projects p1
    LEFT JOIN Projects p2
    ON (p1.End_Date = p2.Start_Date)
    WHERE p2.Start_Date IS NULL) AS t2
WHERE t1.row_num = t2.row_num
ORDER BY DATEDIFF(ed, sd), sd


