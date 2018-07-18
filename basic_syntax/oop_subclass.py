# coding=utf-8

class SchoolMember:
    '''代表任何学校里的成员。'''
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print"(Initialized SchoolMember: {})".format(self.name)

    def tell(self):
        '''告诉我有关我的细节。'''
        print'Name:"{}" Age:"{}"'.format(self.name,self.age)

class Teacher(SchoolMember):
    """代表一位老师。"""
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print"(Initialized Teacher: {})".format(self.name)

    def tell(self):
        SchoolMember.tell(self)
        print'Salary: "{:d}"'.format(self.salary)

class Student(SchoolMember):
    '''代表一位学生'''
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks
        print"(Initialized Student: {})".format(self.name)

    def tell(self):
        SchoolMember.tell(self)
        print'Marks: "{:d}"'.format(self.marks)


t = Teacher('Mrs. Shrividya',40,30000)
s = Student('Swaroop',25,75)

# 打印一行空白行
print

members = [t,s]
# 对全体师生工作
# 会发现此处是调用的子类自己的tell方法，因为Python总会从当前的实际类型中开始寻找方法，
# 如果找不到对应的方法，就会在该类的超类中依序逐个寻找
for member in members:
    member.tell()

