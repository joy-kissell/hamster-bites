import pandas as pd
cleanData = pd.read_csv('data/hamster_foods.csv')
print(cleanData.head())
print(cleanData.describe())
print(cleanData.dtypes)

duplicates = cleanData[cleanData.duplicated(subset=['food'], keep=False)]
#only print food name
print("duplicates are:" + duplicates['food'])

controversial_foods = cleanData[cleanData['type'] == 'Controversial Foods']['food'].tolist()
print(f"controversial foods: {controversial_foods}")
cleanData = cleanData[cleanData['food'] != 'perfectly safe']
