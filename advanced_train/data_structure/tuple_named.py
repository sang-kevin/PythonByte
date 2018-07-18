# name the element in the tuple

student = ('sangyu', '22', 'male', 'sy@qq.com')
print student[0]
print student[1]
print student[2]

# method one
name, age, sex, email = xrange(4)
print student[name]
print student[age]
print student[sex]

# method two
from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])
s = Student('sangyu', '22', 'male', 'sy@qq.com')
print s
print s.name
print s.age

s2 = Student(name='xueqin', age='22', sex='female', email='xq@qq.com')
print s2

print isinstance(s, tuple)  # s is subclass of tuple
