# coding=utf-8
from bs4 import BeautifulSoup
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# 根据HTML网页字符串创建BeautifulSoup对象
soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')
print('>>>>获取所有的链接')
links = soup.find_all('a')
for link in links:
    print link.name, link['href'], link.get_text()

print('>>>>获取Lacie的链接')
link_node = soup.find('a', href="http://example.com/lacie")
print link_node.name, link_node['href'], link_node.get_text()

print('>>>>正则表达式匹配')
link_node = soup.find('a', href=re.compile(r"ill"))  # 加r是因为如果正则表达式中出现了反斜线的话，只需要写一个反斜线
print link_node.name, link_node['href'], link_node.get_text()  # find_all和find查找的结果为节点（整个）

print('>>>>获取p段落文字')
p_node = soup.find('p', class_="title")
print p_node.name,p_node['class'], p_node.get_text()
