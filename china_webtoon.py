import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
list_url = 'http://ac.qq.com/Comic/all/search/hot/page'

html = requests.get(list_url).text
soup = BeautifulSoup(html, 'html.parser')

import mechanicalsoup
browser = mechanicalsoup.StatefulBrowser()

import re
for pages_num in range(1,50) :
    {'search.page' : pages_num}

    list_url = 'http://ac.qq.com/Comic/all/search/hot/page/' + str(pages_num)
    soup = browser.open(list_url).soup

    for tag in soup.select('div.ret-works-info'):
        name = tag.select('h3.ret-works-title.clearfix a')[0].text
        people = tag.select('p.ret-works-tags span em')[0].text
        writer = tag.select('p.ret-works-author')[0].text
        book_url = urljoin(list_url, tag.find('a')['href'])
        book_soup = browser.open(book_url).soup
        print(name + "◎" ,people+  "◎", book_url+  " ◎", end="")
        try:
            body = book_soup.select('.works-intro-short')[0].text
            body_1 = re.sub(r'^\s+','',body)
            body_2 = re.sub('\n',' ',body_1)
            body_3 = " ".join(body_2.split())
            print(body_3+ "◎", end="")
        except IndexError as e:
            print(e, "◎", end="")
        a = 0
        while a < len(tag.select('p.ret-works-tags a')) :
            n = len(tag.select('p.ret-works-tags a'))
            print(tag.select('p.ret-works-tags a')[a].text, "◎",end='')
            a = a+1
            if a == n:
                break
        print()
