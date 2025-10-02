import pandas as pd
pd.__version__
import numpy as np

# Define the URL of the raw CSV file
url = 'https://raw.githubusercontent.com/alexeygrigorev/datasets/master/car_fuel_efficiency.csv'

# Read the data directly from the URL into a DataFrame
df = pd.read_csv(url)

df.shape
df.columns
df['fuel_type'].nunique()
df.isnull().sum()
df[df['origin'] == 'Asia']['fuel_efficiency_mpg'].max()

# Calculate the initial median
initial_median = df['horsepower'].median()
# Find the most frequent value (mode)
horsepower_mode = df['horsepower'].mode()[0]
# Fill missing values with the mode
df['horsepower'] = df['horsepower'].fillna(horsepower_mode)
# Calculate the new median
final_median = df['horsepower'].median()



# 1. Select all cars from Asia ('Japan') and specific columns.
# 2. Select the first 7 values.
subset = df[df['origin'] == 'Asia'][['vehicle_weight', 'model_year']].head(7)

# 3. Get the underlying NumPy array.
X = subset.to_numpy()

# 4. Compute matrix-matrix multiplication between the transpose of X and X.
XTX = X.T @ X

# 5. Invert XTX.
XTX_inv = np.linalg.inv(XTX)

# 6. Create array y.
y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])

# 7. Multiply the inverse of XTX with X.T, and then by y.
w = (XTX_inv @ X.T) @ y

# 8. Calculate the sum of all the elements of the result.
final_sum = w.sum()

print(f"The calculated weight vector w is: {w}")
print(f"The final sum of the elements in w is: {final_sum}")
