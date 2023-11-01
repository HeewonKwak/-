-- Advanced Select / Binary Tree Nodes
-- https://www.hackerrank.com/challenges/binary-search-tree-1/problem?isFullScreen=true
/*
Enter your query here.
*/
WITH bb AS (
SELECT
b2.N AS n1,
b1.N AS n2,
b1.P AS n3
FROM BST b1
LEFT JOIN BST b2
ON (b1.N = b2.P))

SELECT
DISTINCT n2 AS NODE,
CASE
    WHEN n1 IS NULL THEN "Leaf"
    WHEN n3 IS NULL THEN "Root"
    ELSE "Inner"
END AS Type
FROM bb
ORDER BY NODE