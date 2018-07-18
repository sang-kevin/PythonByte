# s = input('Enter something --> ')
# import sys
# print(sys.version_info)
# print(sys.version_info.major == 3)
def get_error_details():
    return (2, 'details')
errnum, errstr = get_error_details()
print(errnum)
print(errstr)

a = 5;b=8
print(a,b)
a, b = b, a
print(a,b)

flag = True
if flag: print('Yes')

print "a = %s" % b
print "a = %s, b = %s" % (b, a)
import logging as logger
logger.debug("I know a = %s and b = %s", (b, a))
