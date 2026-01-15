SELECT account_number, COUNT(*) AS high_value_txns
FROM transactions
WHERE amount > 1000
GROUP BY account_number
HAVING high_value_txns > 5;
