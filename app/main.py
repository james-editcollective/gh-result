from fastapi import FastAPI, Request, Response

from .db import models
from .db.sessions import SessionLocal, engine

from .router import gh_result

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(gh_result.router)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


@app.get("/")
async def root():
    return {"response": "success"}
