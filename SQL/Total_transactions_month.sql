SELECT MONTH(transaction_date) AS month, COUNT(*) AS total_txns
FROM transactions
GROUP BY month
ORDER BY month;
