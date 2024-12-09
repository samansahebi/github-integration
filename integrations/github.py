import aiohttp
from fastapi import HTTPException


class Github:

    def __init__(self):
        self.version = {'version': 'v0.0.1'}
        self.host = 'https://api.github.com'

    async def get_organization_repositories(self, **params):
        async with aiohttp.ClientSession() as session:
            url = f"{self.host}/orgs/{params['org']}/repos"
            session.headers.update({"Accept": "application/vnd.github+json"})
            session.headers.update({"Authorization": f"Bearer {params['token']}"})
            session.headers.update({"X-GitHub-Api-Version": "2022-11-28"})
            async with session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data
                else:
                    raise HTTPException(status_code=resp.status, detail=resp.reason)

    async def get_repository(self, **params):
        async with aiohttp.ClientSession() as session:
            url = f"{self.host}/repos/{params['owner']}/{params['repo']}"
            session.headers.update({"Accept": "application/vnd.github+json"})
            session.headers.update({"Authorization": f"Bearer {params['token']}"})
            session.headers.update({"X-GitHub-Api-Version": "2022-11-28"})
            async with session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data
                else:
                    raise HTTPException(status_code=resp.status, detail=resp.reason)

    async def get_user_repositories(self, **params):
        async with aiohttp.ClientSession() as session:
            url = f"{self.host}/users/{params['user']}/repos"
            session.headers.update({"Accept": "application/vnd.github+json"})
            session.headers.update({"Authorization": f"Bearer {params['token']}"})
            session.headers.update({"X-GitHub-Api-Version": "2022-11-28"})
            async with session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data
                else:
                    raise HTTPException(status_code=resp.status, detail=resp.reason)

    async def get_file_content(self, **params):
        async with aiohttp.ClientSession() as session:
            url = f"{self.host}/repos/{params['owner']}/{params['repo']}/contents/{params['path']}"
            session.headers.update({"Accept": "application/vnd.github.object+json"})
            session.headers.update({"Authorization": f"Bearer {params['token']}"})
            session.headers.update({"X-GitHub-Api-Version": "2022-11-28"})
            async with session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data
                else:
                    raise HTTPException(status_code=resp.status, detail=resp.reason)

    async def get_all_repositories(self, **params):
        async with aiohttp.ClientSession() as session:
            url = f"{self.host}/repos/{params['owner']}/{params['repo']}/commits/{params['ref']}"
            session.headers.update({"Accept": "application/vnd.github+json"})
            session.headers.update({"Authorization": f"Bearer {params['token']}"})
            session.headers.update({"X-GitHub-Api-Version": "2022-11-28"})
            async with session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data
                else:
                    raise HTTPException(status_code=resp.status, detail=resp.reason)

    async def get_repository_branches(self, **params):
        async with aiohttp.ClientSession() as session:
            url = f"{self.host}/repos/{params['owner']}/{params['repo']}/branches"
            session.headers.update({"Accept": "application/vnd.github+json"})
            session.headers.update({"Authorization": f"Bearer {params['token']}"})
            session.headers.update({"X-GitHub-Api-Version": "2022-11-28"})
            async with session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data
                else:
                    raise HTTPException(status_code=resp.status, detail=resp.reason)

    async def get_repository_contributors(self, **params):
        async with aiohttp.ClientSession() as session:
            url = f"{self.host}/repos/{params['owner']}/{params['repo']}/contributors"
            session.headers.update({"Accept": "application/vnd.github+json"})
            session.headers.update({"Authorization": f"Bearer {params['token']}"})
            session.headers.update({"X-GitHub-Api-Version": "2022-11-28"})
            async with session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data
                else:
                    raise HTTPException(status_code=resp.status, detail=resp.reason)

    async def get_repository_deployments(self, **params):
        async with aiohttp.ClientSession() as session:
            url = f"{self.host}/repos/{params['owner']}/{params['repo']}/deployments"
            session.headers.update({"Accept": "application/vnd.github+json"})
            session.headers.update({"Authorization": f"Bearer {params['token']}"})
            session.headers.update({"X-GitHub-Api-Version": "2022-11-28"})
            async with session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data
                else:
                    raise HTTPException(status_code=resp.status, detail=resp.reason)
