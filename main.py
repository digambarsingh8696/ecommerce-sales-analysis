# E-commerce Sales Data Analysis Project for Resume

# Step 1: Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load Dataset (replace with your CSV file path)
df = pd.read_csv('ecommerce_sales.csv')  # Simulated dataset of online orders

# Step 3: Initial Data Inspection
print(df.head())
print(df.info())
print(df.describe())

# Step 4: Data Cleaning
# Convert order date to datetime
df['order_date'] = pd.to_datetime(df['order_date'])

# Drop rows with missing values
df.dropna(inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Step 5: Feature Engineering
# Create new column for revenue
df['revenue'] = df['price'] * df['quantity']

# Extract month and day of week
df['month'] = df['order_date'].dt.month
df['day_of_week'] = df['order_date'].dt.day_name()

# Step 6: Exploratory Data Analysis
# Revenue by month
monthly_revenue = df.groupby('month')['revenue'].sum()
monthly_revenue.plot(kind='bar', title='Monthly Revenue')
plt.ylabel('Revenue')
plt.xlabel('Month')
plt.show()

# Top 10 selling products
top_products = df.groupby('product_name')['quantity'].sum().sort_values(ascending=False).head(10)
top_products.plot(kind='barh', title='Top 10 Selling Products')
plt.xlabel('Quantity Sold')
plt.show()

# Revenue by category
category_revenue = df.groupby('category')['revenue'].sum()
category_revenue.plot(kind='pie', autopct='%1.1f%%', title='Revenue by Category')
plt.ylabel('')
plt.show()

# Orders by weekday
weekday_orders = df['day_of_week'].value_counts().loc[['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']]
weekday_orders.plot(kind='bar', title='Orders by Day of Week')
plt.ylabel('Number of Orders')
plt.xlabel('Day')
plt.show()

# Step 7: Key Insights
# (Print statements for resume explanation)
print("\n--- Key Insights ---")
print("1. Highest revenue month:", monthly_revenue.idxmax())
print("2. Top selling product:", top_products.idxmax())
print("3. Category contributing most to revenue:", category_revenue.idxmax())
print("4. Busiest shopping day:", weekday_orders.idxmax())

# Step 8: Optional - Export Cleaned Data
# df.to_csv('cleaned_ecommerce_data.csv', index=False)
