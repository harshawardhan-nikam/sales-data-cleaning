
import pandas as pd
# import the data set
df = pd.read_csv(r"C:\Users\Harshawardhan\Downloads\archive\sales_data.csv")
print(df.head()) #for data set top 5 rows 
print(df.info()) #for data set information 

# Check Missing Values
df.isnull().sum()

# removing of duplicates
print("Duplicates before:", df.duplicated().sum())
df.drop_duplicates(inplace=True)
print("Duplicates after:", df.duplicated().sum())

# Standardize Text Columns

text_columns = [ 'Sales_Rep','Region','Product_Category','Customer_Type','Payment_Method','Sales_Channel']
for col in text_columns:
    df[col] = df[col].str.lower().str.strip()

# Convert Date Column to Proper Format

df['Sale_Date'] = pd.to_datetime(df['Sale_Date'])

# Clean Column Names

df.columns = df.columns.str.lower()

# Verify Data Types

df.to_csv("cleaned_sales_data.csv", index=False)

