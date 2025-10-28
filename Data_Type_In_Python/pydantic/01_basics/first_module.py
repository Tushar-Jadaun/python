from pydantic import BaseModel, ValidationError

class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data = {"id": 101, "name": "chai", "is_active": True}

try:
    user = User(**input_data)
    print(user)
except ValidationError as e:
    print(e)
