import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict, StratifiedKFold
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from tabulate import tabulate

# 1. Get user inputs
dataset_path = input("Enter dataset path: ")
n_estimators = int(input("Enter number of decision trees: "))
target_col = input("Enter target column name: ")
n_splits = int(input("Enter number of splits (folds): "))

# 2. Load dataset with encoding fix
try:
    # 'latin1' fixes the UnicodeDecodeError common with Excel/Windows CSVs
    df = pd.read_csv(dataset_path, encoding='latin1')
except Exception as e:
    print(f"Error loading file: {e}")
    exit()

# 3. Display data summary
print("\n" + "="*30)
print(f"Total number of data rows: {len(df)}")
print(f"Total number of columns:   {len(df.columns)}")
print("="*30)

# 4. Prepare Data
# Check if you have an ID or Index column; if so, add it to the drop list
X = df.drop(columns=[target_col])
y = df[target_col]

# Convert categorical text data to numbers (required for Random Forest)
X = pd.get_dummies(X)

# 5. Diagnostic: Check why accuracy is 1.0
# We fit a quick model to see which feature is "leaking" the answer
diag_clf = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
diag_clf.fit(X, y)

#print("\nFeature Importance (If a value is ~1.0, that column is 'cheating'):")
importance_data = [[name, f"{imp:.4f}"] for name, imp in zip(X.columns, diag_clf.feature_importances_)]
#print(tabulate(importance_data, headers=["Feature", "Importance"], tablefmt="grid"))

# 6. Model and Cross-Validation
clf = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
y_pred = cross_val_predict(clf, X, y, cv=cv)

# 7. Metrics Calculation
acc = accuracy_score(y, y_pred)
prec = precision_score(y, y_pred, average='weighted', zero_division=0)
rec = recall_score(y, y_pred, average='weighted', zero_division=0)
f1 = f1_score(y, y_pred, average='weighted', zero_division=0)
cm = confusion_matrix(y, y_pred)

# 8. Print Metrics Table
metrics_table = [
    ["Accuracy", f"{acc:.4f}"],
    ["Precision", f"{prec:.4f}"],
    ["Recall", f"{rec:.4f}"],
    ["F1 Score", f"{f1:.4f}"]
]
print("\nFinal Model Metrics:")
print(tabulate(metrics_table, headers=["Metric", "Value"], tablefmt="grid"))

# 9. Print Confusion Matrix
class_names = sorted(y.unique())
print("\nConfusion Matrix:")
print(tabulate(
    cm,
    headers=[f"Pred {c}" for c in class_names],
    showindex=[f"True {c}" for c in class_names],
    tablefmt="grid"
))
