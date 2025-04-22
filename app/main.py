import os
from dotenv import load_dotenv
from app.routes import users

load_dotenv()

from app.db.db import Base, engine  # todo - move to a separated script
from app.models.user import User  # todo - move to a separated script

Base.metadata.create_all(bind=engine)  # todo - move to a separated script


from fastapi import FastAPI

app = FastAPI(title="Product Feedback API")

app.include_router(users.router, prefix="/users", tags=["Users"])
