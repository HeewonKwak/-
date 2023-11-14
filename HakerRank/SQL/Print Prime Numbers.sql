-- Alternative Queries / Print Prime Numbers
-- https://www.hackerrank.com/challenges/print-prime-numbers/problem?isFullScreen=true
/*
Enter your query here.
*/
WITH numbers AS
(
    SELECT @num:=@num+1 as number FROM
    information_schema.tables t1,
    information_schema.tables t2,
    (SELECT @num:=1) tmp
    LIMIT 1000
)

SELECT
GROUP_CONCAT(number SEPARATOR '&')
FROM numbers
WHERE NOT EXISTS (
    SELECT *
    FROM numbers AS n
    WHERE MOD(numbers.number, n.number) = 0
    AND numbers.number != n.number
);
