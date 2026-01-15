SELECT c.full_name, AVG(t.amount) AS avg_amount
FROM transactions t
JOIN customers c ON t.account_number = c.account_number
GROUP BY c.full_name
HAVING avg_amount > 1000;
