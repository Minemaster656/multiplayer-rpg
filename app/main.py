from fastapi import FastAPI, Request
from app.routers import users, items  # Импорты модулей
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="My Modular API")
app.mount("/static", StaticFiles(directory="app/static"))
templates = Jinja2Templates(directory="app/templates")

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(items.router, prefix="/items", tags=["items"])


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
        },
    )
