from bs4 import BeautifulSoup
import requests

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

article = soup.find('article')
# print(article.prettify)

"""
# get first headline
headline = article.h2.a.text
print(headline)

# get first summary
summary = article.find('div', class_='entry-content').p.text
print(summary)

# get video link
vid_src1 = article.find('iframe', class_='youtube-player')
print(vid_src1)
"""

# get the first video link

vid_src1 = article.find('iframe', class_='youtube-player')
# print(vid_src1) # all inside iframe

vid_src2 = article.find('iframe', class_='youtube-player')['src']
# print(vid_src2) # get the src

vid_id = vid_src2.split('/')[4]
vid_id = vid_id.split('?')[0]
# print(vid_id)

yt_link = f'https://youtube.com/watch?v={vid_id}'
# print(yt_link)


# ===============================================================
# get all headline, summary & video link:

for articles in soup.find_all('article'):
    headline = articles.h2.a.text
    print(headline)

    summary = articles.find('div', class_='entry-content').p.text
    print(summary)

    try:
        vid_src = articles.find('iframe', class_='youtube-player')['src']
        vid_id2 = vid_src.split('/')[4]
        vid_id2 = vid_id2.split('?')[0]
        yt_link2 = f'https://youtube.com/watch?v={vid_id2}'
    except Exception as e:
        yt_link2 = None

    print(yt_link2)

    print()
