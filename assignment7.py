import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load CSV
data = pd.read_csv("/Users/user/Downloads/Assignment 7.csv")

print("\nColumns in CSV:", data.columns)

x_col = 'x(age)'
y_col = 'y(body size)'

# Pearson correlation
correlation_data = data[x_col].corr(data[y_col])
print("\nPearson correlation:", correlation_data)

# Means
x_mean = data[x_col].mean()
y_mean = data[y_col].mean()

# Regression Coefficients
slope = ((data[x_col]-x_mean)*(data[y_col]-y_mean)
         ).sum() / ((data[x_col]-x_mean)**2).sum()
intercept = y_mean - slope * x_mean

# Regression Line
y_pred = intercept + slope * data[x_col]

# Coefficient Of Determination
ss_total = ((data[y_col]-y_mean)**2).sum()
ss_residual = ((data[y_col]-y_pred)**2).sum()
r_squared = 1 - (ss_residual/ss_total)

# Print results
print("\nSlope (b1):", slope)
print("Intercept (b0):", intercept)
print("Coefficient of determination (R^2):", r_squared)
print(f"\nRegression Equation: y = {intercept:.2f} + {slope:.2f}x")

# Plot
plt.scatter(data[x_col], data[y_col], color="blue", label="Actual Data")
plt.plot(data[x_col], y_pred, color="red", label="Regression Line")
plt.xlabel('Age')
plt.ylabel('Body Size')
plt.title('Linear Regression : Age vs Body Size')
plt.legend()
plt.show()
