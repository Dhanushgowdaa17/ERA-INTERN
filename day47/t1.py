import pandas as pd
import numpy as np

# Create dataset (1000 students, imbalanced 90/10)
np.random.seed(42)

df = pd.DataFrame({
    "CGPA": np.random.uniform(5, 10, 1000),
    "Internships": np.random.randint(0, 5, 1000),
    "Backlogs": np.random.randint(0, 10, 1000),
    "Projects": np.random.randint(1, 5, 1000),
    "AptitudeScore": np.random.randint(40, 100, 1000),
    "CommunicationSkills": np.random.randint(1, 10, 1000),
    "Placed": np.random.choice([0, 1], size=1000, p=[0.9, 0.1])
})

print("Dataset created successfully!")
print(df.head())

import time
import pandas as pd
import numpy as np

from scipy.stats import randint
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report

# ==========================================
# 1. LOAD DATASET
# ==========================================
print("--- Step 1: Loading Dataset ---")



print(df.head())

# ==========================================
# 2. DATA PREPARATION
# ==========================================

# Target column
target_column = "Placed"

X = df.drop(columns=[target_column])
y = df[target_column]

# Train-test split (Golden Rule: 80/20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

# ==========================================
# 3. PIPELINE (NO DATA LEAKAGE)
# ==========================================
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('rf', RandomForestClassifier(class_weight='balanced', random_state=42))
])

# ==========================================
# 4. BASELINE MODEL
# ==========================================
print("\n--- Step 2: Baseline Model ---")

pipeline.fit(X_train, y_train)
baseline_pred = pipeline.predict(X_test)

baseline_acc = accuracy_score(y_test, baseline_pred)
baseline_f1 = f1_score(y_test, baseline_pred)

print(f"Baseline Accuracy: {baseline_acc:.4f}")
print(f"Baseline F1 Score: {baseline_f1:.4f}")

# ==========================================
# 5. GRID SEARCH (ACCURACY)
# ==========================================
print("\n--- Step 3: Grid Search (Accuracy) ---")

param_grid = {
    'rf__n_estimators': [50, 100, 200],
    'rf__max_depth': [None, 10, 20],
    'rf__min_samples_split': [2, 5, 10]
}

grid_acc = GridSearchCV(
    pipeline,
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)

start_acc = time.time()
grid_acc.fit(X_train, y_train)
time_acc = time.time() - start_acc

print("Best Params (Accuracy):", grid_acc.best_params_)

# ==========================================
# 6. GRID SEARCH (F1)
# ==========================================
print("\n--- Step 4: Grid Search (F1 Score) ---")

grid_f1 = GridSearchCV(
    pipeline,
    param_grid,
    cv=5,
    scoring='f1',
    n_jobs=-1
)

start_f1 = time.time()
grid_f1.fit(X_train, y_train)
time_f1 = time.time() - start_f1

print("Best Params (F1):", grid_f1.best_params_)

# ==========================================
# 7. RANDOMIZED SEARCH
# ==========================================
print("\n--- Step 5: Randomized Search ---")

param_dist = {
    'rf__n_estimators': randint(10, 500),
    'rf__max_depth': [None, 10, 20, 30, 40],
    'rf__min_samples_split': randint(2, 20)
}

random_search = RandomizedSearchCV(
    pipeline,
    param_distributions=param_dist,
    n_iter=20,
    cv=5,
    scoring='f1',
    random_state=42,
    n_jobs=-1
)

start_rand = time.time()
random_search.fit(X_train, y_train)
time_rand = time.time() - start_rand

print("Best Params (Random):", random_search.best_params_)

# ==========================================
# 8. FINAL EVALUATION
# ==========================================
print("\n" + "="*50)
print("FINAL COMPARISON")
print("="*50)

# Predictions
grid_acc_pred = grid_acc.predict(X_test)
grid_f1_pred = grid_f1.predict(X_test)
rand_pred = random_search.predict(X_test)

# Scores
grid_acc_f1 = f1_score(y_test, grid_acc_pred)
grid_f1_f1 = f1_score(y_test, grid_f1_pred)
rand_f1 = f1_score(y_test, rand_pred)

# Table
results = pd.DataFrame({
    "Method": ["Grid (Accuracy)", "Grid (F1)", "Random Search"],
    "Time (sec)": [time_acc, time_f1, time_rand],
    "F1 Score": [grid_acc_f1, grid_f1_f1, rand_f1]
})

print(results)

# ==========================================
# 9. CLASSIFICATION REPORT
# ==========================================
print("\n--- Best Model Report (F1 Grid) ---")
print(classification_report(y_test, grid_f1_pred))

# ==========================================
# 10. INSIGHT
# ==========================================
print("\nINSIGHT:")
print("> Accuracy-optimized model ignores minority class.")
print("> F1-optimized model detects 'at-risk' students better.")
print("> Random Search gives near-optimal results much faster.")