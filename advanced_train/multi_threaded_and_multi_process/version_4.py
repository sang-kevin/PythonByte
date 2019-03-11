# coding=utf-8
# version 4：在线程间进行事件通知（即发送信号）
# 可以使用标准库中Threading.Event
# 等待事件一端调用wait, 等待事件
# 通知事件一端调用 set, 通知事件
# TarThread线程如何退出？  把TarThread设置为守护线程，即其它线程退出后，python程序（进程）就结束了，不需要等待守护线程的结束。
# 设置方法：在构造器中：self.setDaemon(True)

import tushare as ts
import csv
from xml.etree.ElementTree import Element, ElementTree
from threading import Thread, Event
from Queue import Queue
import tarfile
import os


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
    def __init__(self, queue, cEvent, tEvent):
        Thread.__init__(self)
        self.queue = queue
        self.cEvent = cEvent
        self.tEvent = tEvent

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
        count = 0
        while True:
            # 需要从生产者ConvertThread获取的数据：sid, cfname
            sid, cfname = self.queue.get()
            print 'Convert to XML...(%s)' % sid
            if sid == 'finished':
                self.cEvent.set()
                self.tEvent.wait()
                break
            xfname = sid + '.xml'
            self.csvToXml(cfname, xfname)
            count += 1

            if count == 3:
                self.cEvent.set()

                self.tEvent.wait()
                self.tEvent.clear()
                count = 0


class TarThread(Thread):
    def __init__(self, cEvent, tEvent):
        Thread.__init__(self)
        self.count = 0
        self.cEvent = cEvent
        self.tEvent = tEvent
        self.setDaemon(True)

    def tarXML(self):
        self.count += 1
        tfname = '%d.tar.gz' % self.count
        tf = tarfile.open(tfname, 'w:gz')
        for fname in os.listdir('.'):
            if fname.endswith('.xml'):
                tf.add(fname)
                os.remove(fname)
        tf.close()

        if not tf.members:
            os.remove(tfname)

    def run(self):
        while True:
            self.cEvent.wait()
            self.tarXML()
            self.cEvent.clear()

            self.tEvent.set()


if __name__ == '__main__':
    q = Queue()
    dthreads = []
    for sid in ['000875', '600848', '000981', '600606', '002285']:
        t = DownloadThread(sid, q)
        dthreads.append(t)
        t.start()

    cEvent = Event()
    tEvent = Event()

    cThread = ConvertThread(q, cEvent, tEvent)
    cThread.start()

    tThread = TarThread(cEvent, tEvent)
    tThread.start()

    for t in dthreads:
        t.join()
    q.put(('finished', None))

    print 'main thread'  # 主线程可能会比cThread子线程先退出
