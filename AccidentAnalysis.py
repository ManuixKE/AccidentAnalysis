# -*- coding: utf-8 -*-
"""Copy of Welcome to Colaboratory

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UohL6j63nIUpeuI8gOEieU7xdoCRJiAs
"""

import pandas as pd

data = {
    'Weather': ['Clear', 'Rainy', 'Snowy', 'Rainy', 'Clear', 'Clear', 'Snowy', 'Rainy'],
    'Road_Surface': ['Dry', 'Wet', 'Wet', 'Dry', 'Dry', 'Wet', 'Wet', 'Dry'],
    'Light_Condition': ['Daylight', 'Night', 'Daylight', 'Night', 'Daylight', 'Night', 'Daylight', 'Night'],
    'Speed_Limit': [50, 60, 40, 30, 70, 20, 60, 50],
    'Age_of_Driver': [30, 45, 25, 50, 35, 55, 28, 40],
    'Vehicle_Type': ['Car', 'Motorcycle', 'Truck', 'Bus', 'Car', 'Motorcycle', 'Truck', 'Bus'],
    'Accident_Severity': [1, 2, 3, 2, 1, 3, 3, 2]
}

df = pd.DataFrame(data)
df.to_csv('road_accidents.csv', index=False)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle


data = pd.read_csv('road_accidents.csv')


data['Weather'] = data['Weather'].map({'Clear': 0, 'Rainy': 1, 'Snowy': 2}).fillna(-1)
data['Road_Surface'] = data['Road_Surface'].map({'Dry': 0, 'Wet': 1}).fillna(-1)
data['Light_Condition'] = data['Light_Condition'].map({'Daylight': 0, 'Night': 1}).fillna(-1)
data['Vehicle_Type'] = data['Vehicle_Type'].map({'Car': 0, 'Motorcycle': 1, 'Bus': 2, 'Truck': 3}).fillna(-1)


X = data[['Weather', 'Road_Surface', 'Light_Condition', 'Speed_Limit', 'Age_of_Driver', 'Vehicle_Type']]
y = data['Accident_Severity']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)

with open('road_accident_severity_model.pkl', 'wb') as f:
    pickle.dump(model, f)

hypothetical_data = pd.DataFrame([[1, 1, 1, 60, 45, 0]],
                                  columns=['Weather', 'Road_Surface', 'Light_Condition', 'Speed_Limit', 'Age_of_Driver', 'Vehicle_Type'])

predicted_severity = model.predict(hypothetical_data)
print(f'Predicted Accident Severity: {predicted_severity[0]}')