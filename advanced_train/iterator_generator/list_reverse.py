# coding=utf-8

l = [1, 2, 3, 4, 5]

for i in iter(l):
    print i

print '-' * 30

for i in reversed(l):
    print i


class FloatRange:

    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step


for i in FloatRange(1.0, 5.0, 0.5):
    print i

print '-' * 30
for i in reversed(FloatRange(1.0, 5.0, 0.5)):
    print i
