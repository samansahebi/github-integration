import aiohttp
from fastapi import HTTPException


class Github:

    def __init__(self, host, token):
        self.version = {'version': 'v0.0.1',}
        self.host = host
        self.token = token

    async def get_organization_repositories(self, org: str):
        async with aiohttp.ClientSession() as session:
            url = f"https://api.github.com/orgs/{org}/repos"
            session.headers.update({"Accept": "application/vnd.github+json"})
            session.headers.update({"Authorization": f"Bearer {self.token}"})
            session.headers.update({"X-GitHub-Api-Version": "2022-11-28"})
            async with session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data
                else:
                    raise HTTPException(status_code=resp.status, detail=resp.reason)

    async def get_repository(self, owner: str, repo: str):
        async with aiohttp.ClientSession() as session:
            url = f"https://api.github.com/repos/{owner}/{repo}"
            session.headers.update({"Accept": "application/vnd.github+json"})
            session.headers.update({"Authorization": f"Bearer {self.token}"})
            session.headers.update({"X-GitHub-Api-Version": "2022-11-28"})
            async with session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data
                else:
                    raise HTTPException(status_code=resp.status, detail=resp.reason)

    async def get_user_repositories(self, user: str):
        async with aiohttp.ClientSession() as session:
            url = f"https://api.github.com/users/{user}/repos"
            session.headers.update({"Accept": "application/vnd.github+json"})
            session.headers.update({"Authorization": f"Bearer {self.token}"})
            session.headers.update({"X-GitHub-Api-Version": "2022-11-28"})
            async with session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data
                else:
                    raise HTTPException(status_code=resp.status, detail=resp.reason)

    async def get_file_content(self, owner: str, repo: str, path: str):
        async with aiohttp.ClientSession() as session:
            url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
            session.headers.update({"Accept": "application/vnd.github.object+json"})
            session.headers.update({"Authorization": f"Bearer {self.token}"})
            session.headers.update({"X-GitHub-Api-Version": "2022-11-28"})
            async with session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data
                else:
                    raise HTTPException(status_code=resp.status, detail=resp.reason)

    async def get_all_repositories(self, owner: str, repo: str, ref: str):
        async with aiohttp.ClientSession() as session:
            url = f"https://api.github.com/repos/{owner}/{repo}/commits/{ref}"
            session.headers.update({"Accept": "application/vnd.github+json"})
            session.headers.update({"Authorization": f"Bearer {self.token}"})
            session.headers.update({"X-GitHub-Api-Version": "2022-11-28"})
            async with session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data
                else:
                    raise HTTPException(status_code=resp.status, detail=resp.reason)

    async def get_repository_branches(self, owner: str, repo: str):
        async with aiohttp.ClientSession() as session:
            url = f"https://api.github.com/repos/{owner}/{repo}/branches"
            session.headers.update({"Accept": "application/vnd.github+json"})
            session.headers.update({"Authorization": f"Bearer {self.token}"})
            session.headers.update({"X-GitHub-Api-Version": "2022-11-28"})
            async with session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data
                else:
                    raise HTTPException(status_code=resp.status, detail=resp.reason)

    async def get_repository_contributors(self, owner: str, repo: str):
        async with aiohttp.ClientSession() as session:
            url = f"https://api.github.com/repos/{owner}/{repo}/contributors"
            session.headers.update({"Accept": "application/vnd.github+json"})
            session.headers.update({"Authorization": f"Bearer {self.token}"})
            session.headers.update({"X-GitHub-Api-Version": "2022-11-28"})
            async with session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data
                else:
                    raise HTTPException(status_code=resp.status, detail=resp.reason)

    async def get_repository_deployments(self, owner: str, repo: str):
        async with aiohttp.ClientSession() as session:
            url = f"https://api.github.com/repos/{owner}/{repo}/deployments"
            session.headers.update({"Accept": "application/vnd.github+json"})
            session.headers.update({"Authorization": f"Bearer {self.token}"})
            session.headers.update({"X-GitHub-Api-Version": "2022-11-28"})
            async with session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data
                else:
                    raise HTTPException(status_code=resp.status, detail=resp.reason)
