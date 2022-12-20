from enum import Enum
from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from config import settings
from db.database import Base, engine
from db.main import db_router


templates = Jinja2Templates(directory="templates")

def include_router(app):
    app.include_router(db_router)

def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")

def create_tables():
	Base.metadata.create_all(bind=engine)

def start_application():
	app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
	include_router(app)
	configure_static(app)
	create_tables()
	return app

app = start_application()

@app .get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})