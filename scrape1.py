from bs4 import BeautifulSoup
import requests

with open('scrape1.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

"""
# basic
print(soup)

# indented
print(soup.prettify())

# get title
match_title = soup.title
match_title_text = soup.title.text
print(match_title)
print(match_title_text)

# using find to get first div
match_div = soup.find('div')
print(match_div.prettify())  # .prettify() may be deleted

# using find to get div with specific class
match_divclass = soup.find('div', class_='footer')
print(match_divclass.prettify())  # .prettify() may be deleted

article = soup.find('div', class_='article')
# print(article.prettify())  # .prettify() may be deleted

headline = article.h2.a.text
print(headline)

summary = article.p.text
print(summary)
"""

# get all specific element, not just the first
for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    print()
