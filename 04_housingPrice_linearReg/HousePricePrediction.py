import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Load the dataset
data = pd.read_csv('housing.csv')

# Check for missing values
print("Missing values:\n", data.isnull().sum())


# Remove outliers using IQR for 'price' and 'area'
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]


data = remove_outliers(data, 'price')
data = remove_outliers(data, 'area')
print(f"Data shape after outlier removal: {data.shape}")

# Apply log-transformation to price
data['price'] = np.log1p(data['price'])  # log1p handles zero/negative values safely

# Initialize LabelEncoder for categorical columns
le_dict = {}
categorical_cols = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea',
                    'furnishingstatus']
for col in categorical_cols:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    le_dict[col] = le

# Define features and target
X = data.drop('price', axis=1)
y = data['price']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Hyperparameter tuning with GridSearchCV
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5]
}
grid_search = GridSearchCV(RandomForestRegressor(random_state=42), param_grid, cv=5, scoring='r2', n_jobs=-1)
grid_search.fit(X_train, y_train)
model = grid_search.best_estimator_
print(f"Best parameters: {grid_search.best_params_}")

# Predictions (on log scale)
y_pred = model.predict(X_test)

# Transform predictions back to original scale
y_test_exp = np.expm1(y_test)  # Inverse of log1p
y_pred_exp = np.expm1(y_pred)

# Evaluate model
mse = mean_squared_error(y_test_exp, y_pred_exp)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test_exp, y_pred_exp)
r2 = r2_score(y_test_exp, y_pred_exp)

print("\nModel Evaluation Metrics (Original Price Scale):")
print(f"MSE: {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"MAE: {mae:.2f}")
print(f"R²: {r2:.4f}")


# Function to predict price based on user input
def predict_house_price():
    print("\nEnter house details for price prediction:")
    area = float(input("Area (sq ft): "))
    bedrooms = int(input("Number of bedrooms: "))
    bathrooms = int(input("Number of bathrooms: "))
    stories = int(input("Number of stories: "))
    mainroad = input("Main road (yes/no): ").lower()
    guestroom = input("Guest room (yes/no): ").lower()
    basement = input("Basement (yes/no): ").lower()
    hotwaterheating = input("Hot water heating (yes/no): ").lower()
    airconditioning = input("Air conditioning (yes/no): ").lower()
    parking = int(input("Number of parking spaces: "))
    prefarea = input("Preferred area (yes/no): ").lower()
    furnishingstatus = input("Furnishing status (furnished/semi-furnished/unfurnished): ").lower()

    # Encode categorical inputs
    input_data = [
        area, bedrooms, bathrooms, stories,
        le_dict['mainroad'].transform([mainroad])[0],
        le_dict['guestroom'].transform([guestroom])[0],
        le_dict['basement'].transform([basement])[0],
        le_dict['hotwaterheating'].transform([hotwaterheating])[0],
        le_dict['airconditioning'].transform([airconditioning])[0],
        parking,
        le_dict['prefarea'].transform([prefarea])[0],
        le_dict['furnishingstatus'].transform([furnishingstatus])[0]
    ]

    # Scale input
    input_scaled = scaler.transform([input_data])

    # Predict (log scale) and transform back
    predicted_price_log = model.predict(input_scaled)[0]
    predicted_price = np.expm1(predicted_price_log)
    print(f"\nPredicted House Price: ₹{predicted_price:,.2f}")


# Run prediction
if __name__ == "__main__":
    predict_house_price()