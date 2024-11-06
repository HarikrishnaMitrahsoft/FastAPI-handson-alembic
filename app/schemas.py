from pydantic import BaseModel, Field
from typing import Optional

class ProfileBase(BaseModel):
    bio: Optional[str] = None

class ProfileCreate(ProfileBase):
    pass

class Profile(ProfileBase):
    profile_id: int
    user_id: Optional[int] = None

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    user_id: int
    profile: Optional[Profile] = None

    class Config:
        orm_mode = True
