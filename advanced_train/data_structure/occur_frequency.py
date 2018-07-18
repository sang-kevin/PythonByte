# Frequency of elements in the sequence

from random import randint
data = [randint(0, 20) for _ in xrange(20)]
print data

# method one
d = dict.fromkeys(data, 0)
print d

for x in data:
    d[x] += 1
print d

# method two
from collections import Counter
c = Counter(data)
print c
print c.most_common(3)  # most frequent


# Word frequency for acticle
txt = open('files/coding-style.rst.txt').read()
print txt

import re
c2 = Counter(re.split(r'\W+', txt))
print c2
print c2.most_common(5)
