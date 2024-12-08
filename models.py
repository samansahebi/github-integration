from sqlmodel import SQLModel, Field, Session, select, create_engine


class Parameters(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str = Field(nullable=False)
    key: str = Field(nullable=False)
    value: str = Field(nullable=False)
    type: str = Field(nullable=False)
    is_ref: bool = Field(nullable=False)

    def __str__(self):
        return self.key

    def list(self, db: Session):
        statement = select(self.model)
        result = db.execute(statement)
        return result.all()


class Actions(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str = Field(max_length=100)
    slug: str = Field(max_length=100)
    description: str = Field(max_length=100)
    parameters: str = Field(max_length=100)
    created_at: str = Field(max_length=100)
    updated_at: str = Field(max_length=100)

    def __str__(self):
        return self.title

    async def list(self, db: Session):
        statement = select(self.model)
        result = db.execute(statement)
        return result.all()

    async def get(self, db: Session, slug: str):
        statement = select(self.model).where(self.slug == slug)
        result = db.execute(statement).first()
        return result

    async def create_action(self, action):
        return Actions(title=action, method=action.method, description=action.description, parameters=action.parameters)

    async def action_trigger(self, slug: str):
        pass


engine = create_engine(f'postgresql://postgres:postgres@localhost:5432/postgres')
SQLModel.metadata.create_all(engine)

