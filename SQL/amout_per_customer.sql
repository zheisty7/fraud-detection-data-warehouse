SELECT c.full_name, SUM(t.amount) AS total_spent
FROM transactions t
JOIN customers c ON t.account_number = c.account_number
GROUP BY c.full_name
ORDER BY total_spent DESC
LIMIT 10;
