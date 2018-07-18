import requests


def download(url):
    defined_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
             Chrome/67.0.3396.99 Safari/537.36'
    }
    response = requests.get(url, headers=defined_headers)
    print response
    print '--' * 30
    print response.status_code
    print '--' * 30
    print response.headers
    print '--' * 30
    print response.request
    print '--' * 30
    print response.request.headers
    print '--' * 30
    print response.content


if __name__ == '__main__':
    url = 'https://movie.douban.com/subject/1292052/'
    download(url)
