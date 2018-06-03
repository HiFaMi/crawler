

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'lxml')

# #print(html_doc)
# print(soup.prettify())

print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.find_all('p'))
for anchor in soup.find_all('a'):
    print(anchor.get('href'))
