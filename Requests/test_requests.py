# coding=utf-8
import Requests

# Requests库使用了urllib3（多次请求重复使用一个socket)

URL_GET = 'http://httpbin.org/get'
URL_IP = 'http://httpbin.org/ip'


def use_simple_requests():
    response = Requests.get(URL_IP)
    print('>>>>Response Headers:')
    print(response.headers)
    print('Response Body:')
    print(response.text)


def use_params_requests():
    # 构建请求参数
    params = {'param1': 'hello', 'param2': 'world'}
    # 发送请求
    response = Requests.get(URL_GET, params)
    # 处理响应
    print('>>>>Response Headers:')
    print(response.headers)
    print('>>>>Status Code:')
    print(response.status_code)
    print(response.reason)
    print('Response Body:')
    print(response.json())


if __name__ == '__main__':
    print('>>>>use params requests:')
    use_params_requests()
    print('>>>>use simple requests:')
    use_simple_requests()
