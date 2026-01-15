SELECT c.full_name, ROUND(AVG(t.amount), 2) AS avg_transaction
FROM transactions t
JOIN customers c ON t.account_number = c.account_number
GROUP BY c.full_name
ORDER BY avg_transaction DESC
LIMIT 10;
