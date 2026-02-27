from pydantic import BaseModel
from typing import Optional

class Car(BaseModel):
    car_brand:str
    car_type:str
    life_span:float
    weight:Optional[float] 

car1={'car_brand':'tyota','car_type':'advanture','life_span':10,'weight':'893'}
new_car = Car(**car1)
print(new_car)