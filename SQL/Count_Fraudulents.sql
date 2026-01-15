SELECT is_fraudulent, COUNT(*) AS count
FROM transactions
GROUP BY is_fraudulent;
