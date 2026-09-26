import pandas as pd

df = pd.read_csv("data/marketing_sales_dataset.csv")

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

df['discount_percentage'] = df['discount_percentage'].fillna(0)
df['customer_satisfaction_score'] = df['customer_satisfaction_score'].fillna(df['customer_satisfaction_score'].mean())
df['email_open_rate'] = df['email_open_rate'].fillna(0)
df['days_since_last_purchase'] = df['days_since_last_purchase'].fillna(0)

print(df.isnull().sum())

print(df.groupby('region')['sales_revenue_usd'].sum().sort_values(ascending=False))

print(df.groupby('region')['sales_revenue_usd'].agg(['sum', 'mean', 'count']).sort_values('sum', ascending=False))
