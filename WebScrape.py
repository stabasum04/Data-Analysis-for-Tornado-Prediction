import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://starlust.org/messier-catalog/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table')
data = []

# Iterate through the rows of the table
for row in table.find_all('tr'):
    cols = row.find_all('td')
    if len(cols) > 0:
        # Extract data from columns
        m = cols[0].text
        ngc = cols[1].text
        obj_type = cols[2].text
        cons = cols[3].text
        ra = cols[4].text
        dec = cols[5].text
        mag = cols[6].text
        size = cols[7].text
        dist_ly = cols[8].text
        season = cols[9].text
        difficulty = cols[10].text
        
        data.append([m, ngc, obj_type, cons, ra, dec, mag, size, dist_ly, season, difficulty])


columns = ["M", "NGC", "Type", "Cons", "RA", "Dec", "Mag", "Size", "Dist(ly)", "ViewingSeason", "ViewingDifficulty"]
df = pd.DataFrame(data, columns=columns)
df.to_csv('Scrapped_dataset.csv')

