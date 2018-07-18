# sort dict according to value

from random import randint

d = {k: randint(0, 20) for k in 'abcdef'}
print d
print sorted(d)
print d.keys()
print d.values()

print d.iterkeys()
print list(d.iterkeys())

# method one
print zip(d.keys(), d.values())
print zip(*zip(d.keys(), d.values()))

print sorted(zip(d.itervalues(), d.iterkeys()))

# method two
print d.items()
print sorted(d.items(), key=lambda x:x[1])
