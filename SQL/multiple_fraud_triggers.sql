SELECT account_number, COUNT(*) AS fraud_count
FROM transactions
WHERE is_fraudulent = 1
GROUP BY account_number
HAVING fraud_count > 1;
