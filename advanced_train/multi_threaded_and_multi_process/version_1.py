# coding=utf-8
# version 1 :下载.csv格式的文件并转换为.xml格式

import tushare as ts
import csv
from xml.etree.ElementTree import Element, ElementTree


def download(sid, cfname):
    df = ts.get_hist_data(sid)
    df.to_csv(cfname)


def csvToXml(cfname):
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

    return ElementTree(root)


if __name__ == '__main__':
    sid = '000875'
    cfname = sid + '.csv'
    xfname = sid + '.xml'

    download(sid, cfname)
    et = csvToXml(cfname)
    et.write(xfname)
