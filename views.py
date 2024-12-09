import aiohttp
from fastapi import APIRouter, Request, HTTPException
from sqlmodel import select, Session

from integrations.github import Github
from models import Actions, engine


router = APIRouter()


@router.get("/actions")
async def list_actions():
    with Session(engine) as session:
        actions = select(Actions)
        result = session.execute(actions).all()

        return {"action": [list(res) for res in result]}


@router.get("/actions/{slug}", response_model=Actions)
async def list_actions(slug: str):
    with Session(engine) as session:
        actions = select(Actions).where(Actions.slug == slug)
        result = session.execute(actions).first()
        return {"action": result}


@router.post("/actions", response_model=Actions)
async def create_actions(actions: Actions):
    with Session(engine) as session:
        act = Actions(title=actions.title, description=actions.description, slug=actions.slug, parameters=actions.parameters)
        session.add(act)
        session.commit()
        return {"action": act}


@router.post("/actions/{slug}", response_model=Actions)
async def create_actions(actions: Actions, slug: str):
    with Session(engine) as session:
        if slug.startswith('github'):
            statement = select(Actions).where(Actions.slug == slug)
            action = session.execute(statement).first()
            token = action.parameters.filter(key='token').token
            host = 'https://github.com'
            if not token:
                raise HTTPException(401, 'Invalid token')
            integration = Github(host=host, token=token)
            result = getattr(integration, actions.method)()
            return {"result": result}
