-- SQL Injection Detection

SELECT *
FROM web_logs
WHERE url LIKE '%UNION SELECT%'
	OR url LIKE '%DROP TABLE%'
	OR url LIKE '% OR 1=1%'
	OR url LIKE '%--%'
	OR url LIKE "%' OR%"
	OR user_agent LIKE '%sqlmap%';

-- Suspicious IPs

SELECT
	ip_address,
	COUNT(*) AS suspicious_requests
FROM web_logs
WHERE url LIKE '%UNION SELECT%'
	OR url LIKE '%DROP TABLE%'
	OR url LIKE '% OR 1=1%'
	OR url LIKE '%--%'
	OR url LIKE '% OR%'
	OR user_agent LIKE '%sqlmap%'
GROUP BY ip_address
ORDER BY suspicious_requests DESC;

-- Failed Logins

SELECT *
FROM web_logs
WHERE url LIKE '%login%'
	AND status_code = 401;

-- Server Errors

SELECT *
FROM web_logs
WHERE status_code >=500;
