# IPL Score Prediction - Predicting Total Runs using IPL Dataset

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import seaborn as sns
from matplotlib import pyplot as plt

# 1. Load the dataset
df = pd.read_csv('ipl.csv')

# 2. Basic EDA (Exploratory Data Analysis)
print(df.head())

print(df.info())

print(df.describe())

print(df.columns)

print("\nDataset Shape:", df.shape)
print("\nDataset Index:", df.index)

# 3. Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# 4. Remove columns that are not required for prediction
cols_to_remove = ['mid', 'venue', 'batsman', 'bowler', 'striker', 'non-striker']
df.drop(columns=cols_to_remove, axis=1, inplace=True)
print("\nShape after removing unnecessary columns:", df.shape)

#  Display unique teams
teams = df['bat_team'].unique()
print("\nUnique Batting Teams:", teams)

#  Remove first 5 overs data in every match (as per common IPL analysis practice)
df = df[df['overs'] > 5]

#  Convert 'date' column to datetime object
df['date'] = pd.to_datetime(df['date'])


df_corr = df.corr(numeric_only=True)
# 5. Plot heatmap of the dataset
plt.figure(figsize=(12, 8))
sns.heatmap(df_corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap of IPL Dataset")
plt.show()

#  One-hot encode categorical columns ('bat_team' and 'bowl_team')
df_encoded = pd.get_dummies(df, columns=['bat_team', 'bowl_team'])


X = df_encoded.drop(['total'], axis=1)
y = df_encoded['total']

#dropping date as it not works with scikit-learn
X.drop(columns=['date'], inplace=True)

#  Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining set shape:", X_train.shape)
print("Test set shape:", X_test.shape)

# Train a Linear Regression model
lr = LinearRegression()
lr.fit(X_train, y_train)

# Make predictions on the test set
y_pred = lr.predict(X_test)

# Evaluate the model
mae= (mean_absolute_error(y_test, y_pred))
print(f"Mean absolute error: {mae:.2f}")


# Plot Actual vs Predicted Total Runs
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.5, color='blue')
plt.xlabel("Actual Total Runs")
plt.ylabel("Predicted Total Runs")
plt.title("Actual vs Predicted Total Runs")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.show()

