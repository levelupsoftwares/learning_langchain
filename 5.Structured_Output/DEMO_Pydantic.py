from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    name:str
    age:Optional[int]= None   #Optional value set if the value isnt provide 

new_student = {'name':'12'}
student =Student(**new_student)
print(student)