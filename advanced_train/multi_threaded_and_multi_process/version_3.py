# coding=utf-8
# version 3：
# 使用多个DownloadThread线程进行下载（I/0操作）
# 使用一个ConvertThread线程进行转换（CPU密集型）

import tushare as ts
import csv
from xml.etree.ElementTree import Element, ElementTree
from threading import Thread
from Queue import Queue


class DownloadThread(Thread):
    def __init__(self, sid, queue):
        Thread.__init__(self)
        self.sid = sid
        self.cfname = sid + '.csv'
        self.queue = queue

    def download(self, sid, cfname):
        df = ts.get_hist_data(sid)
        df.to_csv(cfname)

    def run(self):
        print 'Download...(%s)' % self.sid
        self.download(self.sid, self.cfname)
        # 需要传给消费者的数据：(sid, cfname)
        self.queue.put((self.sid, self.cfname))


class ConvertThread(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def csvToXml(self, cfname, xfname):
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

    def run(self):
        while True:
            # 需要从生产者ConvertThread获取的数据：sid, cfname
            sid, cfname = self.queue.get()
            print 'Convert to XML...(%s)' % sid
            if sid == 'finished':
                break
            xfname = sid + '.xml'
            self.csvToXml(cfname, xfname)


if __name__ == '__main__':
    q = Queue()
    dthreads = []
    for sid in ['000875', '600848', '000981', '600606', '002285']:
        t = DownloadThread(sid, q)
        dthreads.append(t)
        t.start()

    cThread = ConvertThread(q)
    cThread.start()

    for t in dthreads:
        t.join()
    q.put(('finished', None))

    print 'main thread'  # 主线程可能会比cThread子线程先退出
