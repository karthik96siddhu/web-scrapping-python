import requests
from bs4 import BeautifulSoup

page = requests.get('https://dataquestio.github.io/web-scraping-pages/simple.html')

soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())
# print(list(soup.children))
# print([type(item) for item in list(soup.children)])

html = list(soup.children)[2]
# print(html)
# print(list(html.children))

body = list(html.children)[3]
# print(body)
# print(list(body.children))

p = list(body.children)[1]

# print(p.get_text())

# Find all instance of tag once
# print(soup.find_all('p'))
# print(soup.find_all('p')[0].get_text())

# To find first instance of tag
# print(soup.find('p'))


# Searching for Tags by class and ids
page2  = requests.get("https://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup2 = BeautifulSoup(page2.content, 'html.parser')
# print(soup2)
# print(soup2.find_all('p', class_='outer-text'))
# print(soup2.find_all(class_='outer-text'))
# print(soup2.find_all(id="first")[0].get_text())
print(soup2.select('div p'))



