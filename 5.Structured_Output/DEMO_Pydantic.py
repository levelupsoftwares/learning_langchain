from pydantic import BaseModel ,EmailStr ,Field
from typing import Optional

class Student(BaseModel):
    name:str
    age:Optional[int]= None   #Optional value set if the value isnt provide 
    email:EmailStr
    CGPA:float = Field(gt=2,lt=4 ,default=2 ,description='the float value respresent the cgpa')

new_student = {'name':'12','email':'abc@gmail.com' , 'CGPA':3}

student =Student(**new_student)

student_dict = dict(student)
# print(student_dict)
student_json = student.model_dump_json() # 

print(student_json)
# print(student.email , student.CGPA)