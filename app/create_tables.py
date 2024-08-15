from sqlalchemy import MetaData
from sqlalchemy.schema import CreateTable
from app.backend.db import engine, Base
from app.models.task import Task
from app.models.user import User


# Создание всех таблиц в базе данных
Base.metadata.create_all(bind=engine)

# Печать SQL-запросов для создания таблиц
metadata = MetaData()
print(CreateTable(Task.__table__).compile(engine))
print(CreateTable(User.__table__).compile(engine))
