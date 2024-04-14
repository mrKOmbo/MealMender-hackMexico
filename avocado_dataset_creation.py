import pandas as pd
import numpy as np
import os

# Setting the start date and end date
start_date = '1990-01-01'
end_date = '2020-12-31'

# Create the date range
dates = pd.date_range(start=start_date, end=end_date, freq='4MS')  # '4MS' - every 4 months at month start
print(dates)
# Generate random values with a growth trend
np.random.seed(42)  # For reproducibility
base = 50
y_values = [base + i + np.random.randint(-5, 5)*2 for i in range(len(dates))]  # Simulate growth with random fluctuations

# Create the DataFrame
df = pd.DataFrame({
    'ds': dates,
    'y': y_values
})

# Show the DataFrame
print(df.head())

# Save the DataFrame to an Excel file
file_path = 'C:\\Users\\ruyca\\Desktop\\MealMender-hackMexico\\avocado_consumption.xlsx'

print(file_path)
# Update the path as needed
df.to_excel(file_path, index=False, engine='openpyxl')

print(f'DataFrame saved to {file_path}')