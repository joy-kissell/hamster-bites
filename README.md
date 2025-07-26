# Hamster Bites
Database of foods that hamsters can/cannot eat, including frequency and controversiality.
## Setup
pip install -r requirements.txt
## Progress
scraped all food items from webpage into dataframe and saved to a csv: https://ontariohamsters.ca/education/Food-safety.html
current columns: food (name), type (fruit, vegetable, protein, miscellaneous, controversial, dangerous), safe (yes, no, controversial)
    TODO: data cleaning
        -get rid of controversial foods type and if not in another type already, sort food item and mark safe
        -controversial true/false column?
        -details in parenthesis-->own column or add cooked/raw column
        -multiple item names with slashes-->separate into different food items if not synonyms