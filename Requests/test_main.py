# coding=utf-8
import json
import Requests
from Requests import exceptions

URL = 'https://api.github.com'


def build_url(endpoint):
    return '/'.join([URL, endpoint])


def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)


def request_method():
    # token = {"Authorization": "aab270cd6a55d32ad9e0217ea40a86adfb5bad8f"}
    # response = requests.get('https://api.github.com/user', headers=token)
    # response = requests.get(build_url('users/sangyu1996'))
    response = Requests.get(build_url('user/emails'), auth=('sangyu1996', 'sangyu@1996'))
    print(better_print(response.text))


def params_request():
    response = Requests.get(build_url('users'), params={'since': 5})
    print(better_print(response.text))
    print(response.request.headers)
    print(response.url)


def json_request():
    # response = requests.patch(build_url('user'), auth=('sangyu1996', 'sangyu@1996'),
    #                           json={'name': 'sangyu199603', 'company': 'DXC'})
    response = Requests.post(build_url('user/emails'), auth=('sangyu1996', 'sangyu@1996'),
                             json=['sang@dxc.com'])
    print(better_print(response.text))
    print
    print(response.request.headers)
    print
    print(response.request.body)
    print
    print(response.status_code)


def timeout_request():
    try:
        response = Requests.get(build_url('user/emails'), timeout=10)
        if True:
            response.raise_for_status()  # 如果发送了一个失败请求(非200响应)，我们可以通过该式来抛出异常
    except exceptions.Timeout as e:
        print e.message
    except exceptions.HTTPError as e:
        print e.message
    else:
        print(response.text)
        print(response.status_code)
        print


if __name__ == '__main__':
    timeout_request()
