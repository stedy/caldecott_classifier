from bs4 import BeautifulSoup
import wikipedia
import requests
import os
import pandas as pd

base = wikipedia.page("This_is_Not_My_Hat")
print(base.images)

img = list(filter(lambda x: 'cover' in x, base.images))
r = requests.get(img[0])
#open(img[0], 'wb').write(r.content)

#os.system('wget {}'.format(img[0]))

base_url="https://en.wikipedia.org/wiki/Caldecott_Medal"
response = requests.get(base_url)

soup = BeautifulSoup(response.text, 'html.parser')
booktable = soup.find('table', {'class':"wikitable"})
df = pd.read_html(str(booktable), extract_links = True)

print(df)
