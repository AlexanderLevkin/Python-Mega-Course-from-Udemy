import pandas as pd

df = pd.read_csv("../Day_31_App_6_Build_a_Historical_Weather_Data_API_with_Python_(Part_3)/wines.csv")

max_rating = df['points'].max()
count_max_rating = df[df['points'] == max_rating].shape[0]

max_cost = df['price'].max()
name_max_cost = df.loc[df['price'] == df['price'].max()]['name'].squeeze()



print(max_rating)
print(name_max_cost)
print(count_max_rating)
