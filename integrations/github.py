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
