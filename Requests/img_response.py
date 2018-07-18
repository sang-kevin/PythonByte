# coding=utf-8
import requests


def download_image():
    """
    demo：下载图片
    """
    url = 'http://a.hiphotos.baidu.com/image/pic/item/ac345982b2b7d0a224a30f4fc1ef76094a369afd.jpg'
    defined_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
    response = requests.get(url, headers=defined_headers, stream=True)
    with open('demo.jpg', 'wb') as f:
        for chunk in response.iter_content(128):  # response中有这个API可以遍历它的所有的内容
            f.write(chunk)


# 增加一个上下文的语境，因为这里用到的是流传递，所以在结束时需要把流关掉，这里就用到了语法糖（contextlib）中的closing
def download_image_improved():
    """
    下载图片
    """
    # 伪造headers信息
    defined_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
    # 限定URL
    url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1514444573077&di=d5e47681a66390ab69219bf90da3b179&imgtype=0&src=http%3A%2F%2Fres.ladyband.com%2F2017%2F12-04%2F04%2F8f83658941851d439f7c9709a7040d1c.jpg'
    from contextlib import closing
    with closing(requests.get(url, headers=defined_headers, stream=True)) as response:
        with open('demo1.jpg', 'wb') as f:
            for chunk in response.iter_content(128):
                f.write(chunk)


if __name__ == '__main__':
    # download_image()
    download_image_improved()
