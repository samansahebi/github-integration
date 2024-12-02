from pydantic import BaseModel


class AuthenticateByUserPass(BaseModel):
    username: str
    password: str
