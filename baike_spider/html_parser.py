# coding=utf-8
import re
import urlparse

from bs4 import BeautifulSoup


class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # /item/Python
        links = soup.find_all('a', href=re.compile(
            r"/item/(.*)"))  # r的作用：后面的字符串中的字符不需要转义，不当做转义字符，直接就是原字符串;何为转义字符：顾名思义，改变意思。将本来的是数字或者字母的意思改变为某一个命令。
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url,
                                            new_url)  # urljoin主要是拼接URL，它以base作为其基地址，然后与url中的相对地址相结合组成一个绝对URL地址
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        # url
        res_data['url'] = page_url

        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')  # 树形结构，在class="lemmaWgt-lemmaTitle-title"的element的子元素去查找
        res_data['title'] = title_node.get_text()                                    # class 在Python中是保留字,使用 class 做参数会导致语法错误.

        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
