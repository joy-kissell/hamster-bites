import pandas as pd
cleanData = pd.read_csv('data/hamster_foods.csv')
print(cleanData.head())
print(cleanData.describe())
print(cleanData.dtypes)