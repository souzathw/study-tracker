from fastapi import FastAPI
from app.api.routes import auth
from app.db.session import engine
from app.db.base import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

#Rotas
app.include_router(auth.router, prefix="/auth", tags=["auth"])

