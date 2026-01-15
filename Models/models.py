import pandas as pd
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. LOAD DATA
customers = pd.read_csv(r"/Users/zach/Desktop/School/Fall '25/DATA 415/Project 1/customers.csv")
transactions = pd.read_csv(r"/Users/zach/Desktop/School/Fall '25/DATA 415/Project 1/transactions.csv")

# 2. CLEAN & PREPARE DATES
transactions["transaction_date"] = pd.to_datetime(transactions["transaction_date"])
customers["date_of_birth"] = pd.to_datetime(customers["date_of_birth"])

# 3. FEATURE ENGINEERING
# Compute age from DOB
today = datetime.now()
customers["age"] = customers["date_of_birth"].apply(lambda dob: (today - dob).days // 365)

# 4. JOIN DATASETS
df = transactions.merge(customers, on="account_number", how="left")

# Encode gender
le_gender = LabelEncoder()
df["gender"] = le_gender.fit_transform(df["gender"].astype(str))

# Sort by date for prior calculations
df = df.sort_values(by="transaction_date")

# 5. CREATE PRIOR ALERTS FEATURE
df["prior_alerts"] = df.groupby("account_number")["is_fraudulent"].cumsum() - df["is_fraudulent"]

# 6. CREATE PRIOR FRAUDS FEATURE
df["prior_frauds"] = df.groupby("account_number")["is_fraudulent"].cumsum() - df["is_fraudulent"]

# 7. DEFINE FEATURES AND TARGET
X = df[["amount", "age", "gender", "prior_alerts", "prior_frauds"]]
y = df["is_fraudulent"]

# 8. TRAIN/TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# 9. SCALE NUMERIC FEATURES
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 10. MODEL 1 — LOGISTIC REGRESSION
logreg = LogisticRegression(max_iter=2000, class_weight='balanced')
logreg.fit(X_train_scaled, y_train)
logreg_preds = logreg.predict(X_test_scaled)

print("LOGISTIC REGRESSION")
print("Accuracy:", accuracy_score(y_test, logreg_preds))
print(classification_report(y_test, logreg_preds, zero_division=0))

# 11. MODEL 2 — DECISION TREE
tree = DecisionTreeClassifier(max_depth=5, class_weight='balanced')
tree.fit(X_train, y_train)
tree_preds = tree.predict(X_test)

print("\nDECISION TREE")
print("Accuracy:", accuracy_score(y_test, tree_preds))
print(classification_report(y_test, tree_preds, zero_division=0))

# 12. MODEL 3 — K-NEAREST NEIGHBORS
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)
knn_preds = knn.predict(X_test_scaled)

print("\nKNN")
print("Accuracy:", accuracy_score(y_test, knn_preds))
print(classification_report(y_test, knn_preds, zero_division=0))

# 13. SAVE FINAL MERGED DATASET
df.to_csv(r"/Users/zach/Desktop/School/Fall '25/DATA 415/Project 1/final_merged_dataset.csv", index=False)
print("\nSaved final_merged_dataset.csv")
