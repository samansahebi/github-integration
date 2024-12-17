from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}
#
# @router.get("/actions")
# async def list_actions():
#     with Session(engine) as session:
#         actions = select(Actions)
#         result = session.execute(actions).all()
#
#         return {"action": [list(res) for res in result]}
#
#
# @router.get("/actions/{slug}", response_model=Actions)
# async def list_actions(slug: str):
#     with Session(engine) as session:
#         actions = select(Actions).where(Actions.slug == slug)
#         result = session.execute(actions).first()
#         return {"action": result}
#
#
# @router.post("/actions", response_model=Actions)
# async def create_actions(actions: Actions):
#     with Session(engine) as session:
#         act = Actions(title=actions.title, description=actions.description, slug=actions.slug, parameters=actions.parameters)
#         session.add(act)
#         session.commit()
#         return {"action": act}
#
#
# @router.post("/actions/{slug}", response_model=Actions)
# async def create_actions(slug: str):
#     async with Session(engine) as session:
#         if slug.startswith('github'):
#             statement = select(Actions).where(Actions.slug == slug)
#             action = await session.execute(statement).first()
#             params = dict()
#             for param in action.parameters:
#                 params[param.key] = param.value
#             integration = Github()
#             result = await getattr(integration, action.method, **params)
#             return {"result": result}
