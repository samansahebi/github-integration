import aiohttp
from fastapi import APIRouter, Request, HTTPException
from models import Actions


router = APIRouter()


@router.get("/actions", response_model=list[Actions])
async def list_actions(actions: Actions):
    return {"action": actions.get_actions()}


@router.get("/actions/{action}", response_model=Actions)
async def list_actions(actions: Actions, action: str):
    return {"action": actions.get_action(action)}


@router.post("/actions", response_model=Actions)
async def create_actions(actions: Actions):
    act = actions.create_action(actions)
    return {"action": act}


@router.post("/actions/{action}", response_model=Actions)
async def create_actions(actions: Actions, action: str):
    if actions.get_action(action):
        act = actions.action_trigger(actions)
        return {"action": act}


@router.get("/orgs/{org}/repos")
async def get_organization_repositories(request: Request, org: str):
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
async def get_repository(request: Request, owner: str, repo: str):
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
async def get_user_repositories(request: Request, user: str):
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
async def get_file_content(request: Request, owner: str, repo: str, path: str):
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


@router.get("/repos/{owner}/{repo}/branches")
async def get_repository_branches(request: Request, owner: str, repo: str):
    async with aiohttp.ClientSession() as session:
        url = f"https://api.github.com/repos/{owner}/{repo}/branches"
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


@router.get("/repos/{owner}/{repo}/contributors")
async def get_repository_contributors(request: Request, owner: str, repo: str):
    async with aiohttp.ClientSession() as session:
        url = f"https://api.github.com/repos/{owner}/{repo}/contributors"
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


@router.get("/repos/{owner}/{repo}/deployments")
async def get_repository_deployments(request: Request, owner: str, repo: str):
    async with aiohttp.ClientSession() as session:
        url = f"https://api.github.com/repos/{owner}/{repo}/deployments"
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
