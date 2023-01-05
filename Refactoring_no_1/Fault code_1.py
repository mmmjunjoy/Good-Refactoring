from bs4 import BeautifulSoup
import requests

url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=리팩토링'
Response = requests.get(url)
html=Response.text
soup=BeautifulSoup(html, 'lxml')
articleContainer = soup.find('ul',class = 'type01')
articles = articleContainer.findAll('li')
title = []
for article in articles:
    dt = article.find('dt')
    if dt is not None:
        continue
    title = dt.find('a').text
    titles.append(title)

with open('result.txt','w') as result:
    for title in titles:
        result.write(title + '\n')