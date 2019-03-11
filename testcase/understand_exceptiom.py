def occer_exception():
    try:
        d = dict()
        d['name'] = 'sy'
        d['age'] = '23'
        print d.pop('name')
        print d['hometown']
        print d.pop('age')
    except Exception as e:
        print 'an error occured for %s' % e
        raise e


if __name__ == '__main__':
    try:
        print 'test start'
        occer_exception()
    except Exception as e:
        print 'capture the error thrown by the calling function for %s' % e
        print "except clause end"
    print "finished"
