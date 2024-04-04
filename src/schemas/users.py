from pydantic import BaseModel


class UserRead(BaseModel):
    id: str
    full_name: str
    email: str
    is_active: bool
    is_superuser: bool
    is_verified: bool
