# coding=utf-8

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):  # 传入的data是一个集合{}
        if data is None:
            return
        self.datas.append(data)

    # datas列表中不一定有一千个元素，同样output.html中也就不会有一千行了
    def output_html(self):
        fout = open('output_format.html', 'w')
        fout.write('<html>')
        # fout.write('<head><meta charset="utf-8"></head>') # 有没有这行并不影响html页面的显示效果
        fout.write('<body>')
        fout.write('<table width="300%">')
        for data in self.datas:  # 每一个页面的的数据为一个data(是一个集合)放在一行
            fout.write('<tr>')
            fout.write('<td width="40%">{}</td>'.format(data['url']))
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()


""" Python默认的编码是ascii,如果想要输出为UTF-8的话需要加上".encode('utf-8')", 不然有些中文就会识别成乱码

    fout.write('<td>{}</td>'.format(data['title']).encode('utf-8'))
    fout.write('<td>{}</td>'.format(data['summary']).encode('utf-8'))
    这种写法会报错：fout.write('<td>{}</td>'.format(data['summary']).encode('utf-8'))
                    UnicodeEncodeError: 'ascii' codec can't encode character u'\xa0' in position 10: ordinal not in range(128)
    属于python2和python3写法混用了
"""
