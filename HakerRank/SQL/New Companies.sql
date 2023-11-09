-- Advanced Select / New Companies
-- https://www.hackerrank.com/challenges/the-company/problem?isFullScreen=true

/*
Enter your query here.
*/
SELECT
c.company_code,
c.founder,
COUNT(DISTINCT l.lead_manager_code),
COUNT(DISTINCT s.senior_manager_code),
COUNT(DISTINCT m.manager_code),
COUNT(DISTINCT e.employee_code)
FROM Company c,
Lead_Manager l,
Senior_Manager s,
Manager m,
Employee e
WHERE c.company_code = l.company_code and l.lead_manager_code = s.lead_manager_code and s.senior_manager_code = m.senior_manager_code and m.manager_code = e.manager_code
GROUP BY c.company_code, c.founder
ORDER BY c.company_code ASC