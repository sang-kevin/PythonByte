# coding=utf-8
from baike_spider import url_manager, html_downloader, html_parser, html_outputer  # 从包中引入模块（包含函数和变量、以.py为后缀的文件）


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownload()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw{0}:{1}'.format(count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)  # **
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 1000:
                    break
                count = count + 1
            except:
                print'craw failed'
        self.outputer.output_html()


# 在 ** 处触发
# 1、download()传入的new_url is none)
# 2、返回值不为200
# 3、取得的html_cont is none
# 注：new_urls 和 new_data is none 不会报异常，前者只是这次循环不添加新的将要访问的url，后者的影响是生成的html不到一千行

if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/item/Python'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
