class Father(object):
    pass


class Child(Father):
    a = 1


if __name__ == '__main__':
    f = Father()
    print f.a
