-- Alternative Queries / Draw The Triangle 2
-- https://www.hackerrank.com/challenges/draw-the-triangle-2/problem?isFullScreen=true

/*
Enter your query here.
*/
-- 1부터 20까지 찍기
SET @star := 0;
SELECT REPEAT('* ', @star := @star + 1) AS star FROM information_schema.tables
WHERE @star < 20;

-- 20부터 1까지 찍은 것 뒤집기
SET @star := 21;
SELECT REPEAT('* ', @star := @star - 1) AS star FROM information_schema.tables
WHERE @star > 1
ORDER BY star ASC;