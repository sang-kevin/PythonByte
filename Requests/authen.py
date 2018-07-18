# coding=utf-8
import requests

BASE_URL = 'https://api.github.com'


def construct_url(endpoint):
    return '/'.join([BASE_URL, endpoint])


def basic_auth():
    """
    基本认证
    """
    response = requests.get(construct_url('user'), auth=('sangyu1996', 'sangyu@1996'))
    print(response.text)
    print(response.request.headers)


def basic_oauth():
    auth = {'Authorization': 'token aab270cd6a55d32ad9e0217ea40a86adfb5bad8f'}
    # user/emails
    response = requests.get(construct_url('user/emails'), headers=auth)  # headers为内置的，此处必须为headers
    print(response.request.headers)
    print(response.text)
    print(response.status_code)


# requests库提供了一个语法糖
from requests.auth import AuthBase


class GitHubAuth(AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):  # 传给它一个request，此处是类自己定义好的，不需手动传入
        # request 加 headers 的Authorization的信息
        r.headers['Authorization'] = ' '.join(['token', self.token])
        return r


def advanced_oauth():
    auth1 = GitHubAuth('aab270cd6a55d32ad9e0217ea40a86adfb5bad8f')
    response = requests.get(construct_url('user/emails'), auth=auth1)  # auth为内置的，此处必须为auth
    # 为什么auth不需要传入参数r呢？应该是AuthBase类的特殊用法，如果没有特殊用法，这里也没有合适的参数可以传入，无法传入一个request
    print(response.text)


# basic_auth()
# basic_oauth()
advanced_oauth()
