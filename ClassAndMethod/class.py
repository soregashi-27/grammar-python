class Student:

    def __init__(self, name):
        self.name = name

    def avg(self, math, english):
        print((math + english) / 2)


a001 = Student("will")
# a001.avg(30, 70)

print(a001.name)

# a001.gender = "Men"
# print(a001.gender)

a002 = Student("Tanaka")
print(a002.name)

# Attribute and instance
