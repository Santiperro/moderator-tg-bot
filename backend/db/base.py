import re
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


class SnakeCaseMixin:
    @declared_attr.directive
    def __tablename__(cls) -> str:
        name = re.sub(r"(?<!^)(?=[A-Z])", "_", cls.__name__).lower()
        return f"{name}"


class Base(DeclarativeBase, SnakeCaseMixin):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)


DATABASE_URL = "postgresql+psycopg2://user:password@localhost/db_name"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
