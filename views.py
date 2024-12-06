import aiohttp
from fastapi import APIRouter, Request, HTTPException
from github import Github, Auth
from serializers import AuthenticateByUserPass


router = APIRouter()


@router.post("/authenticate")
async def authenticate_user(authenticate: AuthenticateByUserPass):
    auth = Auth.Login(authenticate.username, authenticate.password)
    g = Github(auth=auth)
    g.get_user()
    return {"token": f"{auth.token}"}


@router.get("/orgs/{org}/repos")
async def get_all_repositories(request: Request, org: str):
    async with aiohttp.ClientSession() as session:
        url = f"https://api.github.com/orgs/{org}/repos"
        token = request.headers.get("github-token", None)
        session.headers.update({"Accept": "application/vnd.github+json"})
        session.headers.update({"Authorization": f"Bearer {token}"})
        session.headers.update({"X-GitHub-Api-Version": "2022-11-28"})
        async with session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
                return data
            else:
                raise HTTPException(status_code=resp.status, detail=resp.reason)


@router.get("/repos/{owner}/{repo}")
async def get_all_repositories(request: Request, owner: str, repo: str):
    async with aiohttp.ClientSession() as session:
        url = f"https://api.github.com/repos/{owner}/{repo}"
        token = request.headers.get("github-token", None)
        session.headers.update({"Accept": "application/vnd.github+json"})
        session.headers.update({"Authorization": f"Bearer {token}"})
        session.headers.update({"X-GitHub-Api-Version": "2022-11-28"})
        async with session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
                return data
            else:
                raise HTTPException(status_code=resp.status, detail=resp.reason)


@router.get("/{user}/repos")
async def get_all_repositories(request: Request, user: str):
    async with aiohttp.ClientSession() as session:
        url = f"https://api.github.com/users/{user}/repos"
        token = request.headers.get("github-token", None)
        session.headers.update({"Accept": "application/vnd.github+json"})
        session.headers.update({"Authorization": f"Bearer {token}"})
        session.headers.update({"X-GitHub-Api-Version": "2022-11-28"})
        async with session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
                return data
            else:
                raise HTTPException(status_code=resp.status, detail=resp.reason)


@router.get("/repos/{owner}/{repo}/contents/{path}")
async def get_all_repositories(request: Request, owner: str, repo: str, path: str):
    async with aiohttp.ClientSession() as session:
        url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
        token = request.headers.get("github-token", None)
        session.headers.update({"Accept": "application/vnd.github.object+json"})
        session.headers.update({"Authorization": f"Bearer {token}"})
        session.headers.update({"X-GitHub-Api-Version": "2022-11-28"})
        async with session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
                return data
            else:
                raise HTTPException(status_code=resp.status, detail=resp.reason)


@router.get("/repos/{owner}/{repo}/commits/{ref}")
async def get_all_repositories(request: Request, owner: str, repo: str, ref: str):
    async with aiohttp.ClientSession() as session:
        url = f"https://api.github.com/repos/{owner}/{repo}/commits/{ref}"
        token = request.headers.get("github-token", None)
        session.headers.update({"Accept": "application/vnd.github+json"})
        session.headers.update({"Authorization": f"Bearer {token}"})
        session.headers.update({"X-GitHub-Api-Version": "2022-11-28"})
        async with session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
                return data
            else:
                raise HTTPException(status_code=resp.status, detail=resp.reason)
