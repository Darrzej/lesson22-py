from pydantic import BaseModel , conint, constr
from typing import Optional


# class User(BaseModel):
#     id: int
#     name: str
#     age: int
#     email: str

# user = User(id=1, name="Leon", age=9, email="leonberatjashari@gmail.com")
# print(user)
class User(BaseModel):
    id: int
    name: str
    age: Optional[int] = None
    email: Optional[str] = None

user1 = User(id=1, name="LIO", age=23, email="email@gmail.com")
user2 = User(id=2, name="Seji", email="seji@gmail.com")

print(user1)
print(user2)

class another_user(BaseModel):
    id: conint(gt=0)
    name: constr(min_length=2, max_length=50)

valid_user = another_user(id=1, name="Qamil")  
print(valid_user)

valid_user1 = another_user(id=0, name="Qal")  
print(valid_user1) 