-- Alternative Queries / Draw The Triangle 1
-- https://www.hackerrank.com/challenges/draw-the-triangle-1/problem?isFullScreen=true

/*
Enter your query here.
*/
set @star := 21;
SELECT REPEAT('* ', @star := @star - 1) FROM information_schema.tables;