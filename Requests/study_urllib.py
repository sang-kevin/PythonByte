from urllib import request, parse

URL_IP = "http://httpbin.org/ip"
URL_GET = "http://httpbin.org/get"


def use_simple_urllib():
    response = request.urlopen(URL_IP)
    print(">>>>Response Headers:")
    print(response.info())
    print(">>>>Response Body:")
    print(response.read().decode('utf-8'))


def use_params_urllib():
    # 构建请求参数
    params = parse.urlencode({'param1': 'hello', 'param2': 'world'})
    print("Request Params:")
    print(params)
    # 发送请求
    response = request.urlopen("?".join([URL_GET, "%s"]) % params)
    # 处理响应
    print(">>>>Response Headers:")
    print(response.info())
    print(">>>>Response Body:")
    print(response.read().decode('utf-8'))


if __name__ == '__main__':
    print(">>>Use simple urllib:")
    use_simple_urllib()
    print(">>>Use params urllib")
    use_params_urllib()