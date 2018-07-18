# coding-utf-8
# find prime numbers

class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def isPrimeNumber(self, k):
        for i in xrange(2, k):
            if k % i == 0:
                return False
        return True

    def __iter__(self):
        for k in xrange(self.start, self.end + 1):
            if self.isPrimeNumber(k):
                yield k


g = PrimeNumbers(1, 100)
generator_g = g.__iter__()
print generator_g.next()
print generator_g.next()

print '-' * 30

for i in PrimeNumbers(1, 100):
    print i
