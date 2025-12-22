from fastapi import FastAPI
from app.routers import users, items  # Импорты модулей

app = FastAPI(title="My Modular API")

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(items.router, prefix="/items", tags=["items"])


@app.get("/")
def read_root():
    return {"message": "OK"}
