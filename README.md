# Hamster Bites
Database of foods that hamsters can/cannot eat, including frequency and controversiality.
## Setup
pip install -r requirements.txt
## Progress
scraped all food items from webpage into dataframe and saved to a csv: https://ontariohamsters.ca/education/Food-safety.html \
added controversial column (boolean) and got rid of controversial food type\
removed duplicates from dataframe\
current columns: food (name), type (fruit, vegetable, protein, miscellaneous, dangerous), safe (yes/no)\
    TODO: data cleaning\
        -details in parenthesis-->own column or add cooked/raw column\
        -multiple item names with slashes-->separate into different food items if not synonyms\
        -sort dangerous foods and controversial foods into types (placeholder miscellaneous type for now)\
        -create cleaned csv to work with
        -look into changing data types: food-string, type-categorical defined type, safe-binary, controversial-already boolean so good