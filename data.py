import re
import requests
from bs4 import BeautifulSoup
import pandas

url = 'https://www.filarmonicabanatul.ro'

my_headers = {"User-Agent": "Mozilla/5.0"}

page = requests.post(url,headers=my_headers)

soup = BeautifulSoup(page.content, 'html.parser')

tbody = soup.find(class_="eventcalq")

columns = []

for tr in tbody.find_all('td'):

    columns.append([tr for tr in tr.find_all(class_="hasTooltip")])

print(columns)

a=""

for i in columns:
   a=a+str(i)+" "

print(a)

print(re.findall('/strong&gt;&lt;br /&gt;(.*?)&lt',a))

b=re.findall('/strong&gt;&lt;br /&gt;(.*?)&lt',a)

df = pandas.DataFrame({'Evenimente': b,
                      })

print(df)

df.to_csv('evenimente.csv',encoding='utf-8-sig')