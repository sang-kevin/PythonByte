# coding=utf-8
from inspect import signature


def typeassert(*ty_args, **ty_kwargs):
    def decorator(func):
        sig = signature(func)
        btypes = sig.bind_partial(*ty_args,
                                  **ty_kwargs).arguments  # 得到了func的参数和assert的类型对应的字典， OrderedDict([('a', str), ('b', int), ('c', int)])

        def wrapper(*arg, **kwargs):
            for name, value in sig.bind(*arg, **kwargs).arguments.items():
                if name in btypes:
                    if not isinstance(value, btypes[name]):
                        raise TypeError('"%s" nust be "%s"' % (name, btypes[name]))
            return func(*arg, **kwargs)

        return wrapper

    return decorator


@typeassert(int, int, str)
def f(a, b, c):
    print(a, b, c)


f(1, 2, 'abc')


# f(1, 'a', 'b')  # TypeError: "b" nust be "<class 'int'>"


@typeassert(int, str)
def f2(a, b, c):
    print(a, b, c)


f2(1, 2, 'abc')  # TypeError: "b" nust be "<class 'str'>"
