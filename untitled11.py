# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bFdIvBd6MG-VS9OVri5d3YqcM7YXMw4d
"""

# prompt: import /content/Amol Prashant Shirkar - revolutioncart_data.csv

import pandas as pd

# Assuming the file is in the specified path
df = pd.read_csv('/content/Amol Prashant Shirkar - revolutioncart_data.csv')

# Now you can work with the DataFrame 'df'
print(df.head())  # Print the first few rows of the DataFrame

df

# prompt: consider monthly_revenue as y and others as x

x = df.drop('monthly_revenue', axis=1)
y = df['monthly_revenue']

# prompt: split x and y in train and test

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# prompt: make regression model with x_train and y_train

from sklearn.linear_model import LinearRegression

# Create a Linear Regression model
model = LinearRegression()

# Train the model on the training data
model.fit(x_train, y_train)

# prompt: give score

# Evaluate the model on the testing data
score = model.score(x_test, y_test)

print(f"Model Score: {score}")

# prompt: do cross validation

from sklearn.model_selection import cross_val_score

# Perform cross-validation with 5 folds
cv_scores = cross_val_score(model, x, y, cv=5)

# Print the cross-validation scores
print("Cross-validation scores:", cv_scores)

# Print the average cross-validation score
print("Average cross-validation score:", cv_scores.mean())

# prompt: make lasso regression for X_train and y_train

from sklearn.linear_model import Lasso

# Create a Lasso Regression model
lasso_model = Lasso(alpha=0.1)  # You can adjust the alpha value

# Train the model on the training data
lasso_model.fit(x_train, y_train)

# You can now use lasso_model for predictions or further analysis

# prompt: give score

lasso_score = lasso_model.score(x_test, y_test)
print(f"Lasso Model Score: {lasso_score}")

# prompt: do cross validation

from sklearn.model_selection import cross_val_score

# Assuming you have your model (e.g., model) and your data (x, y)

# Perform cross-validation with 5 folds
cv_scores = cross_val_score(model, x, y, cv=5)

# Print the cross-validation scores
print("Cross-validation scores:", cv_scores)

# Print the average cross-validation score
print("Average cross-validation score:", cv_scores.mean())

# prompt: dump model

import pickle

# Save the model to a file
filename = 'linear_regression_model.sav'
pickle.dump(model, open(filename, 'wb'))

# Save the lasso model to a file
filename = 'lasso_regression_model.sav'
pickle.dump(lasso_model, open(filename, 'wb'))