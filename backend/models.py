from sqlalchemy import Column, String, PrimaryKeyConstraint, Integer, Boolean
from database import Base


class Todo(Base):
    __tablename__ = "todos"
    __table_args__ = (
        PrimaryKeyConstraint(
            "id",
        ),
        # {"schema": "test_schema"},
    )
    # fmt: off
    id        = Column(Integer(), primary_key=True, autoincrement=True, index=True, nullable=False)
    name      = Column(String(), nullable=False, default="")
    order     = Column(Integer(), nullable=False, unique=True)
    completed = Column(Boolean(), nullable=False, default=False)
