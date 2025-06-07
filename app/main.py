from fastapi import FastAPI

from app.init_db import init as init_db

from .api.routes.posts import post_router
from .api.routes.users import user_router

init_db()

app = FastAPI(title="Blog API")

app.include_router(post_router)
app.include_router(user_router)
