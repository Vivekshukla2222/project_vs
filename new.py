class Student:
    scholl_name='DPS'
    def __init__(self,name,age):
        self.name=name
        self.age=age

s1=Student("Amit",23)
print(s1.scholl_name)
print(s1.name,s1.age)
