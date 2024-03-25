from pydantic import BaseModel


class UserRead(BaseModel):
    full_name: str
    email: str
    is_active: bool
    is_superuser: bool
