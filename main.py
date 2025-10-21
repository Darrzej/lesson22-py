from pydantic import BaseModel
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