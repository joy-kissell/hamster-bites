# Hamster Bites
Database of foods that hamsters can/cannot eat, including frequency and controversiality.
## Setup
pip install -r requirements.txt
## Data Structure
current columns: food (name), type (fruits, vegetables, proteins, miscellaneous foods), safe (yes/no), controversial (true/false), notes\
## Progress
1.scraped all food items from webpage into dataframe and saved to a csv: https://ontariohamsters.ca/education/Food-safety.html \
2.added controversial column (boolean) and got rid of controversial food type\
3.removed duplicates from dataframe\
4.removed parenthetical names and added notes section with default value 'prepare any way'\
5.got rid of dangerous food type and mapped to vegetables, fruits, proteins, and miscellaneous\

    TODO: data cleaning\
        -multiple item names with slashes-->separate into different food items if not synonyms\
        -sort misc. controversial foods into types \
        -create cleaned csv to work with
        -look into changing data types: food-string, type-categorical defined type, safe-binary, controversial-already boolean so good

## Ideas
create a website so people can add to the database and then post on r/hamsters\
requires setting up a db though so mongodb or sql (decide)\
adding sugar/sodium info from FDA API for predictive modelling of safe/unsafe\