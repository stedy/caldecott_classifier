import os
import requests
import pandas as pd
from bs4 import BeautifulSoup

try:
    os.mkdir("covers")
except FileExistsError:
    pass

base_url="https://en.wikipedia.org/wiki/Caldecott_Medal"
response = requests.get(base_url)

soup = BeautifulSoup(response.text, 'html.parser')
booktable = soup.find('table', {'class':"wikitable"})
df = pd.read_html(str(booktable), extract_links = "all")
df = pd.DataFrame(df[0])

df.columns.values[:] = ["year", "illustrator", "book", "award"]

df2 = pd.DataFrame({'book' : df['book'].str[1] , 'year' : df['year'].str[0] ,
    'award': df['award'].str[0] })
winners = df2[df2['award'] == "Winner"]
winners['year'] = pd.to_numeric(winners['year'])
recent_winners = winners[winners['year'] > 2000]

for x in recent_winners['book']:
    x_year = recent_winners[recent_winners['book'] == x]['year'].values[0]
    r2 = requests.get("https://en.wikipedia.org/" + x)
    soup = BeautifulSoup(r2.text, 'html.parser')
    bookimages = soup.find('meta', {'property':"og:image"})
    FN = str(x_year) + "_" + str(x).strip("/wiki/") + ".jpg"
    FN = ''.join(z for z in FN if z not in '()')
    os.system('wget {} -O {}'.format(bookimages['content'], "covers/" + FN))
