from pydantic import BaseModel, Field, EmailStr


class ContactModel(BaseModel):
    email: EmailStr


class ContactResponse(BaseModel):
    id: int = 1
    email: EmailStr

    class Config:
        orm_mode = True


