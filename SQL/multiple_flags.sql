SELECT c.full_name, t.account_number,
       SUM(CASE WHEN t.is_fraudulent = 1 THEN 1 ELSE 0 END) AS total_frauds,
       AVG(t.amount) AS avg_spend
FROM transactions t
JOIN customers c ON t.account_number = c.account_number
GROUP BY c.full_name, t.account_number
HAVING total_frauds >= 1 OR avg_spend > 900
ORDER BY total_frauds DESC, avg_spend DESC;
