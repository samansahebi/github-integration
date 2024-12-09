from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, create_engine, Relationship


class Parameters(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str = Field(nullable=False)
    key: str = Field(nullable=False)
    value: str = Field(nullable=False)
    type: str = Field(nullable=False)
    is_ref: bool = Field(nullable=False)

    def __str__(self):
        return self.key


class Actions(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str = Field(max_length=100)
    slug: str = Field(max_length=100)
    method: str = Field(max_length=100)
    description: str = Field(max_length=100)
    parameters: list["Parameters"] = Relationship(back_populates="action")
    created_at: Optional[datetime] = Field(default=datetime.utcnow(), nullable=False)
    updated_at: Optional[datetime] = Field(default=datetime.utcnow(), nullable=False)

    def __str__(self):
        return self.title


engine = create_engine(f'postgresql://postgres:postgres@localhost:5432/postgres')
SQLModel.metadata.create_all(engine)

