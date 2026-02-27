from typing import TypedDict

class Student(TypedDict):
    name:str
    age:int
    num:float


student1: Student = {'name':'sim','age':45}
print(student1)
