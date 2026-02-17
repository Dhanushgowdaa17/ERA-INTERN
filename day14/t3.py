import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

np.random.seed(42)

X = np.linspace(-5, 5, 100).reshape(-1, 1)
y = 3*(X**2) + 2*X + 5 + np.random.randn(100, 1)*5

linear_model = LinearRegression()
linear_model.fit(X, y)

y_pred_linear = linear_model.predict(X)
r2_linear = r2_score(y, y_pred_linear)

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

poly_model = LinearRegression()
poly_model.fit(X_poly, y)

y_pred_poly = poly_model.predict(X_poly)
r2_poly = r2_score(y, y_pred_poly)

print("R² Score (Linear Features):", r2_linear)
print("R² Score (Polynomial Features):", r2_poly)
