import csv
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()
Faker.seed(42)
random.seed(42)

# Parameters
NUM_CUSTOMERS = 5000
NUM_TRANSACTIONS = 100000
FRAUD_RATE = 0.009  # less than 1%

# Generate unique customer data
customers = []
customer_accounts = set()

while len(customer_accounts) < NUM_CUSTOMERS:
    # Generate a 10-digit numeric account number
    account_number = str(random.randint(1000000000, 9999999999))
    customer_accounts.add(account_number)

customer_accounts = list(customer_accounts)

for account_number in customer_accounts:
    full_name = fake.name()
    dob = fake.date_of_birth(minimum_age=18, maximum_age=90)
    address = fake.address().replace("\n", ", ")
    occupation = fake.job()
    gender = random.choice(["Male", "Female"])
    
    customers.append({
        "account_number": account_number,
        "full_name": full_name,
        "date_of_birth": dob,
        "address": address,
        "occupation": occupation,
        "gender": gender
    })

# Transaction categories
purchase_categories = [
    "Electronics", "Groceries", "Restaurants", "Clothing",
    "Online Shopping", "Gas Station", "Travel", "Pharmacy",
    "Subscription", "Entertainment", "Luxury Goods"
]

# Define date range
start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 6, 1)

# Select random indices for fraudulent transactions
fraudulent_indices = set(random.sample(range(NUM_TRANSACTIONS), int(NUM_TRANSACTIONS * FRAUD_RATE)))

# Generate transactions
transactions = []

for i in range(NUM_TRANSACTIONS):
    account_number = random.choice(customer_accounts)
    # Random date in range
    random_seconds = random.randint(0, int((end_date - start_date).total_seconds()))
    date = start_date + timedelta(seconds=random_seconds)

    amount = round(random.uniform(5.0, 2000.0), 2)
    category = random.choice(purchase_categories)
    description = f"Purchase at {category}"
    is_fraudulent = 1 if i in fraudulent_indices else 0

    # Find matching customer full name
    full_name = next(c["full_name"] for c in customers if c["account_number"] == account_number)

    transactions.append({
        "account_number": account_number,
        "full_name": full_name,
        "transaction_date": date.strftime("%Y-%m-%d %H:%M:%S"),
        "amount": amount,
        "transaction_type": "Credit Card",
        "transaction_description": description,
        "is_fraudulent": is_fraudulent
    })

# Write customer data to CSV
with open("customers.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=customers[0].keys())
    writer.writeheader()
    writer.writerows(customers)

# Write transaction data to CSV
with open("transactions.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=transactions[0].keys())
    writer.writeheader()
    writer.writerows(transactions)

print("✅ Generated 'customers.csv' and 'transactions.csv' (Jan–Jun 2025, numeric 10-digit accounts).")
