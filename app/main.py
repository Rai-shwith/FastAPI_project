import os
from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from .database import engine
from . import models
from .routers import post,user,auth,vote
from .config import settings
# from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine)



# BASE_DIR = os.path.dirname(os.path.abspath(__file__))


app = FastAPI()
# app.mount("/static",StaticFiles(directory=os.path.join(BASE_DIR,"templates/static")))
app.mount("/static",StaticFiles(directory="app/templates/static"))

app.mount("/signup",StaticFiles(directory="app\\templates\\signup",html=True),name="signup")
app.mount("/login",StaticFiles(directory="app\\templates\\login",html=True),name="login")
app.mount("/addhero",StaticFiles(directory="app\\templates\\addhero",html=True),name="addheroP")
# app.mount("/hero",StaticFiles(directory="app\\templates\moreinfo",html=True),name="moreinfo")
# app.mount("/hero",StaticFiles(directory=os.path.join("app","templates","moreinfo"),html=True),name="moreinfo")



# app.mount("/",StaticFiles(directory=os.path.join(BASE_DIR,"templates"),html=True),name="root")
# app.mount("/",StaticFiles(directory="app/templates",html=True),name="root")

templates = Jinja2Templates(directory="app/templates")


# origins: list[str] = 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root(request : Request):
    return templates.TemplateResponse("index.html",{"request":request})
    return {"message":"hello world"}

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)