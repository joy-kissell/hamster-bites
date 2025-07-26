import requests
from bs4 import BeautifulSoup
import pandas as pd

website = 'https://ontariohamsters.ca/education/Food-safety.html'
response = requests.get(website)
soup = BeautifulSoup(response.content, "html.parser")

food_data= []
#ids to extract items from
ids = ["fruits","vegetables", "proteins", "miscellaneous-foods", "controversial-foods", "dangerous-foods"]

for header in ids:
    section = soup.find(id = header)
    if section:
        ul_element = section.find_next('ul')
        #ul element is right before list starts
        if ul_element:
            items = [li.get_text(strip = True) for li in ul_element.find_all('li')]
            for item in items:
                food_data.append({
                    'food': item,
                    'type': header.replace('-', ' ').title(),
                    'safe': 'no' if header == 'dangerous-foods' else 'controversial' if header == 'controversial-foods' else 'yes'
                })
df = pd.DataFrame(data=food_data)
df.to_csv('hamster_foods.csv', index=False)