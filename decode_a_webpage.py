import requests
from bs4 import BeautifulSoup

url='https://www.nytimes.com/'
r=requests.get(url)
r_html=r.text
print r_html
soup=BeautifulSoup(r.text)
for title in soup.find_all(class_="title"):
    if title.a:
        print(title.a.text.replace("\n", " "))
    else:
        print(title.contents[0])







