# coding=utf-8
# version 2：在每一个线程中下载并转换一只股票数据

import tushare as ts
import csv
from xml.etree.ElementTree import Element, ElementTree
from threading import Thread


def download(sid, cfname):
    df = ts.get_hist_data(sid)
    df.to_csv(cfname)


def csvToXml(cfname, xfname):
    with open(cfname, 'rb') as cf:
        reader = csv.reader(cf)
        headers = reader.next()

        root = Element('Data')
        for row in reader:
            eRow = Element('Row')
            root.append(eRow)
            for tag, text in zip(headers, row):
                e = Element(tag)
                e.text = text
                eRow.append(e)

    et = ElementTree(root)
    et.write(xfname)


def handle(sid):
    cfname = sid + '.csv'
    xfname = sid + '.xml'

    print 'Download...(%s)' % sid
    download(sid, cfname)

    print 'Convert to XML...(%s)' % sid
    csvToXml(cfname, xfname)


class MyThread(Thread):
    def __init__(self, sid):
        Thread.__init__(self)
        self.sid = sid

    def run(self):
        handle(self.sid)


if __name__ == '__main__':
    threads = []
    for sid in ['000875', '600848', '000981', '600606', '002285']:
        t = MyThread(sid)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print 'main thread'
