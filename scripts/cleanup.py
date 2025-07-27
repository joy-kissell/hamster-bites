import pandas as pd
cleanData = pd.read_csv('data/hamster_foods.csv')
print(cleanData.head())
print(cleanData.describe())
print(cleanData.dtypes)

duplicates = cleanData[cleanData.duplicated(subset=['food'], keep=False)]
#only print food name
print("duplicates are:" + duplicates['food'])

cleanData = cleanData[cleanData['food'] != 'perfectly safe']
controversial_foods = cleanData[cleanData['type'] == 'Controversial Foods']['food'].tolist()
print(f"controversial foods: {controversial_foods}")


#getting rid of controversial food type
foodData = cleanData[cleanData['type']!= 'Controversial Foods'].copy()
#boolean column for if food is controversial or not
foodData['controversial'] = foodData['food'].isin(controversial_foods)
for food in controversial_foods:
    #if food is not in cleaned dataframe but is in controversial foods
    if food not in foodData['food'].values:
        #adding row to end of dataframe
        next_index = foodData.index.max() + 1
        foodData.loc[next_index]=[food, "Miscellaneous Foods", 'yes', True]

print(foodData[foodData['controversial']]['food'])
foodData = foodData.drop_duplicates(subset=['food'], keep='first')
print(foodData.describe())