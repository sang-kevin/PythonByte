# coding=utf-8
import requests


# 根据每条请求可以指定一个hook函数通过一个{hook_name: callback_function}字典类型的hook请求参数：
# hooks=dict(response=print_url)
# 可用的hooks：response, 所以hook_name为response,可以理解为会把响应放在字典的key中

def get_key_info(response, *args, **kwargs):
    """
    回调函数
    """
    print(response.headers['Content-Type'])


def main():
    """
    主函数
    """
    requests.get('https://api.github.com',
                 hooks=dict(response=get_key_info))  # 当我接到这个response对象，我要注册一个相应的函数进去，并把response对象作为函数的参数传进去


main()
