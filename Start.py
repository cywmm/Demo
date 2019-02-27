from urllib.request import urlopen, Request
import ssl
import json
import time
import csv
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/50.0.2661.102 Safari/537.36'}
ssl._create_default_https_context = ssl._create_unverified_context

listUrl = json.load(open('宋词精选.json'))

csvFile = open('/Users/wangming/文档/shici/宋词精选.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(csvFile)
writer.writerow(['poemName', 'author', 'dynasty', 'verse', 'interpret', 'comment'])

for i in listUrl:
    key = "contson" + i[32:-5]
    req = Request(i, headers)
    html = urlopen(i).read()
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup)
    content = soup.find("textarea").text

    poemName = content[content.find('《') + 1:content.find('》')]
    author = content[content.find('·') + 1:content.find('《')]
    dynasty = content[content.find('——') + 2:content.find('·')]
    verse = content[0:content.find('——')]

    interpret_txt = soup.find_all('p')[1]
    comment_txt = soup.find_all('p')[2]

    isFindC = "∨" in comment_txt.text
    isFindI = "∨" in interpret_txt.text
    if isFindC:
        comment = comment_txt.text[2:-9]
    else:
        comment = comment_txt.text[2:]

    if isFindI:
        interpret = interpret_txt.text[2:-9]
    else:
        interpret = interpret_txt.text[2:]

    print("诗名：" + poemName)
    print("作者：" + author)
    print("朝代：" + dynasty)
    print("诗句：" + verse)

    print("译文：" + interpret)
    print("注释：" + comment)

    print()

    writer.writerow([poemName, author, dynasty, verse, interpret, comment])
    time.sleep(0.5)
