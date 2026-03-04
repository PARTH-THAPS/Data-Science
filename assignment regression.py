import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("/Users/user/Downloads/Assignment 7.csv")

x_col = 'x(age)'
y_col = 'y(body size)'

x_mean = data["x(age)"].mean()
y_mean = data["y(body size)"].mean()

corelation_Data = data[x_col].corr(data[y_col])
print(corelation_Data)


# Regression Coefficient
slope = ((data[x_col]-x_mean) * (data[y_col] - y_mean)).sum() / \
    ((data[x_col]-x_mean)**2).sum()

print(slope)
intercept = y_mean-slope*data[x_col]

y_pred = intercept + slope * x_mean

ss_residual = ((data[y_col]-y_pred)**2).sum()
