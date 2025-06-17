import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import time
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report,confusion_matrix, roc_auc_score, mean_squared_error,r2_score, accuracy_score
from sklearn.linear_model import LogisticRegression  
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv('C:\\WORKING_FOLDER\\PROJECTS\\TECHVANTO-DS-AIML\\02_10-6-25\\Covid_Dataset.csv')
print(data.head())
print(data.info())
print(data.describe())

#num of rows containing yes
print(data[data['COVID-19'] == 'Yes'].shape[0])

# print((data == 'Yes').any(axis=1).sum())
# df['COVID-19'].value_counts()

# yes_count = covid_data['COVID-19'].value_counts().get('Yes', 0)
# print("Number of rows with 'Yes':", yes_count)

transposed_data = data.T
#diff btwn data.T and data.transpose() and data.describe().T


missing_values = data.isnull().sum()
print("missing values: ", missing_values)

###############           Alter

#heatmap covid-19 and breathing problems
# plt.figure(figsize=(10, 6))
# sns.heatmap(data[['Breathing Problem', 'COVID-19']].corr(), annot=True,cmap='coolwarm')  #will not work as the cols are not numeric
# plt.title("Correlation Heatmap between A and B")
# plt.show()

# using label encoder to convert the whole dataset to numeric values as the whole dataset is just yes and no and label encoder is preloaded to deal with yes no || high medium low || kinda values.


# Initialize LabelEncoder
label_encoder = LabelEncoder()

# Apply Label Encoding to whole dataset
for col in data.columns:
    data[col] = label_encoder.fit_transform(data[col])

#heatmap covid-19 and breathing problems
plt.figure(figsize=(10, 6))
sns.heatmap(data[['Breathing Problem', 'COVID-19']].corr(), annot=True,cmap='coolwarm')  #will  work as the cols are now numeric
plt.title("Correlation Heatmap between Breathing Problem and COVID-19")
plt.show()

#plot a bar graph of covid-19 and breathing problems
plt.figure(figsize=(10, 6))
sns.countplot(x='Breathing Problem', hue='COVID-19', data=data, palette='Set1')
plt.title("Count of COVID-19 cases based on Breathing Problem")
plt.xlabel("Breathing Problem")
plt.ylabel("Count")
plt.legend(title='COVID-19', loc='upper right')
plt.show()

#removing the column "Wearing Masks" 
data_removedMasks = data.drop(columns=['Wearing Masks'])


x=data.drop('COVID-19',axis=1)
y=data['COVID-19']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state = 101)

rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(x_train, y_train)

# predict cases and evauluate

y_pred =rf_model.predict(x_test)
# print("Predicted values: ", y_pred)
# print("Actual values: ", y_test.values) 

mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error: ", mse)


df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

start_date = "22-01-01"

data['date'] = pd.date_range(start=start_date, periods=len(data), freq='D')

future_dates = pd.date_range(start=data['date'].iloc[-1] + pd.Timedelta(days=1), periods=30, freq='D')
print("Future Dates: ", future_dates)

# Predicting future values
future_predictions = rf_model.predict(x.tail(30))

future_df = pd.DataFrame({'date': future_dates, 'Predicted COVID-19 Cases': future_predictions})
print("Future Predictions DataFrame: ")
print(future_df)

