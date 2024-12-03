from pydantic import BaseModel


class AuthenticateByUserPass(BaseModel):
    username: str
    password: str


class GetAllRepositories(BaseModel):
    git_token: str
