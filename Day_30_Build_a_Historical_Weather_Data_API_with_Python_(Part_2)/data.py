# Load the dataframe
import numpy as np
import pandas as pd

df = pd.read_csv('D:\PycharmProjects\Python-Mega-Course-from-Udemy'
                 '\Day_30_Build_a_Historical_Weather_Data_API_with_Python_(Part_2)\data\TG_STAID000001.txt',
                 skiprows=20, parse_dates=["    DATE"])

# Show certain rows

print(df[10:20])

# Show certain columns

print(df.columns)
print(df[['   TG', '    DATE']])


# Simple statistics and filtering

mean = df.loc[df['   TG'] != -9999]['   TG'].mean()
print(mean)

max_filter = df.loc[df['   TG'] != -9999]['   TG'].max()/10
print(max_filter)

min_filter = df.loc[df['   TG'] != -9999]['   TG'].min()/10
print(min_filter)

hist = df.loc[df['   TG'] != -9999]['   TG'].hist()
print(hist)


# Get certain cells
get_certain_cell = df.loc[df['    DATE'] == '1860-01-11']['   TG'].squeeze() / 10
print(get_certain_cell)

by_column_and_row = df.loc[10, '   TG']
print(by_column_and_row)

# Calculate a new colunm out of existing column
# mask - this is without the -9999
df["TG0"] = df["   TG"].mask(df["   TG"] == -9999, np.nan)
df["TG_new"] = df["TG0"] / 10
df["Fahrenheit"] = df["TG_new"] * 9 / 5 + 32

print(df)

# Plotting
df['Fahrenheit'].plot()
