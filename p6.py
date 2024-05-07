import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load data from yfinance
google = yf.Ticker("GOOG")
df = google.history(period="1d", interval="1m")
df = df[["Low"]]
# Extract features and target variable
X = np.arange(len(df)).reshape(-1, 1)
y = df["Low"].values
# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, shuffle=False)
plt.plot(range(0, len(y_train)), y_train, label="Train")
plt.plot(range(len(y_train), len(y)), y_test, label="Test")
plt.legend()
plt.show()
# STEP 2:
# Create a linear regression model
model = LinearRegression()
# Fit the model
model.fit(X_train, y_train)
# Evaluate the model
score = model.score(X_test, y_test)
print("Model score:", score)
# Make predictions
predictions = model.predict(X_test)
# STEP 3:
# Plot the results
plt.plot(X_train, y_train, label="Train")
plt.plot(X_test, y_test, label="Test")
plt.plot(X_test, predictions, label="Predictions")
plt.legend()
plt.show()
# STEP 4:
# Print real data for time 0 (last data point in training set)
print(f"Real data for time 0: {y_train[-1]}")
# Print real data for time 1 (first data point in test set)
print(f"Real data for time 1: {y_test[0]}")
# Use the trained model to predict the data for time 1
forecast = model.predict(X_test[0].reshape(1, -1))[0]
# Print predicted data for time 1
print(f"Predicted data for time 1: {forecast}")
