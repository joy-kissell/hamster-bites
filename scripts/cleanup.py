import pandas as pd
import re
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

#print(foodData[foodData['controversial']]['food'])
foodData = foodData.drop_duplicates(subset=['food'], keep='first')
print(foodData.describe())

#cleaning up parenthesis in food names
def extract_parenthetical(food):
    match = re.search(r'\((.*?)\)', food)
    if match:
        notes = match.group(1)
        fixed_name = re.sub(r'\s*\(.*?\)\s*','',food)
        return fixed_name, notes
    else:
        return food, "prepared any way"
    
foodData[['food', 'notes']] = foodData['food'].apply(
    lambda x: pd.Series(extract_parenthetical(x))
)
#print(foodData[['food', 'notes']])

#getting rid of dangerous food type
dangerous_foods = foodData[foodData['type']== 'Dangerous Foods']['food'].tolist()
#print(dangerous_foods)
mapped_type = ['Proteins', 'Vegetables', 'Fruits', 'Miscellaneous Foods', 'Proteins', 'Vegetables', 'Vegetables']

new_types = dict(zip(dangerous_foods, mapped_type))

mask = foodData['food'].isin(dangerous_foods)
foodData.loc[mask, 'type']= foodData.loc[mask, 'food'].map(new_types)
#checking it's gone
#print(foodData['type'].unique())

#adding more food notes
def cookedDry(food, currentNote):
    if "cooked and dry" in food.lower():
        clean = re.sub(r',?\s*cooked and dry', '', food, flags=re.IGNORECASE).strip()
        if currentNote == "prepared any way":
            newNote = "cooked and dry"
        else:
            newNote = f"{currentNote}, cooked and dry"
        return clean, newNote
    else:
        return food, currentNote
    
foodData[['food', 'notes']]=foodData.apply(
    #apply across rows not columns
    lambda row:pd.Series(cookedDry(row['food'], row['notes'])), axis = 1
)
#print(foodData[['food','notes']].to_string())

#sorting controversial foods into types
print(foodData[foodData['controversial']][['food', 'type', 'notes']])
mappedDict = {'Avocado': 'Fruits', 'Citrus Fruits':'Fruits','Leeks':'Vegetables', 
              'Onions':'Vegetables', 'Raisins':'Fruits', 'Watermelon':'Fruits'}

controversialMask = foodData['food'].isin(mappedDict.keys())
#updating controversial food types
foodData.loc[controversialMask,'type']=foodData.loc[controversialMask,'food'].map(mappedDict)
#checking now
print(foodData[foodData['controversial']][['food', 'type', 'notes']])

#collapsing tomatoes and tomato into 1 row, cucumber and cucumbers into 1 row
foodData.loc[foodData['food']=='Tomato', 'notes']= foodData[foodData['food']== 'Tomatoes']['notes'].iloc[0]
print(foodData[foodData['food']== 'Tomato']['notes'].to_string())
foodData = foodData.drop(foodData[foodData['food']== 'Tomatoes'].index)
# yay it's gone
# print(foodData[foodData['food']== 'Tomatoes'])
foodData = foodData.drop(foodData[foodData['food']=='Cucumbers'].index)
#print(foodData[foodData['food']== 'Cucumbers']['notes'])

#making all food names singular
def singleFood(food):
    food = str(food).strip()
    if len(food)<=3:
        return food
    if food.lower().endswith(('ss', 'us', 'is','ous', 'eens')):
        #e.g. asparagus, cress, greens
        return food
    if food.endswith('ies'):
    #any type or berries
        return food[:-3]+ 'y'
    if food.endswith('s'):
        return food[:-1]
    return food
foodData['food'] = foodData['food'].apply(singleFood)
print(foodData['food'].tolist())

#enforcing data types

ALLOWED_TYPES = ['Fruits', 'Vegetables', 'Proteins', 'Miscellaneous Foods']

def convertDataTypes(df):
    df['food']=df['food'].astype('string')
    #set food types
    df['type']=pd.Categorical(df['type'], categories=ALLOWED_TYPES, ordered = False)
    df['safe']=df['safe'].map({'yes':True, 'no':False}).astype('boolean')
    df['controversial'] = df['controversial'].astype('boolean')
    df['notes'] = df['notes'].astype('string')
    return df

foodData = convertDataTypes(foodData)
print(foodData.dtypes)
print(f"\nType categories: {foodData['type'].cat.categories.tolist()}")
print(f"Type value counts:\n{foodData['type'].value_counts()}")

foodData.to_csv('data/clean_hamster_foods.csv', index=False)