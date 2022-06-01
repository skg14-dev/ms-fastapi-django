import pathlib
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

BASE_DIR = pathlib.Path(__file__).parent

app = FastAPI()
templates = Jinja2Templates(directory=str(BASE_DIR/"templates"))
#every endpoint returns a json by default

@app.get("/", response_class=HTMLResponse)
#need to mention what the variable type is.
def home_view(request: Request):
    return templates.TemplateResponse("home.html",{"request":request,"test":123})
    
@app.post("/")
def home_detail_view():
    return {"hello":"world"}