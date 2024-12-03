from fastapi import APIRouter, HTTPException, Header
import aiohttp
from serializers import GetAllRepositories
from github import Github, Auth
from serializers import AuthenticateByUserPass


router = APIRouter()


@router.post("/authenticate")
async def authenticate_user(authenticate: AuthenticateByUserPass):
    auth = Auth.Login(authenticate.username, authenticate.password)
    return {"token": f"{auth.token}"}


@router.post("/get-all-repositories")
async def get_all_repositories(repositories: GetAllRepositories):
    auth = Auth.Token(token=repositories.git_token)
    g = Github(auth=auth)

    return {"repositories": g.get_repos()}
