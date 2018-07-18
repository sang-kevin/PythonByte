# coding=utf-8
import os
import tarfile


def tarXML(tfname):
    tf = tarfile.open(tfname, 'w:gz')
    for fname in os.listdir('.'):
        if fname.endswith('.xml'):
            tf.add(fname)
            os.remove(fname)  # 添加到打包之后将源文件删除
    tf.close()

    if not tf.members:
        os.remove(tfname)


tarXML('test.tar.gz')  # 或'test.tgz'

# 压缩命令：
# tar -cvf log.tar log2012.log    仅打包，不压缩！
# tar -zcvf log.tar.gz log2012.log   打包后，以 gzip 压缩
# tar -jcvf log.tar.bz2 log2012.log  打包后，以 bzip2 压缩

# 解压缩命令：
# tar -zxvf /opt/soft/test/log.tar.gz -C 要解压到的目录
