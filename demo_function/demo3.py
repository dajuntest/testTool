#encoding:UTF-8
from bs4 import BeautifulSoup
import lxml
import requests


html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')

# print(len(soup.contents[0])[0])
print(soup.contents[0])
# print(soup)
# print(soup.title)
# print(soup.head)
# print((soup.find_all('a')).string)
# print(soup.p)
# print(type(soup.a))