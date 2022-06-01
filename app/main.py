from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
#very endpoint returns a json

@app.get("/", response_class=HTMLResponse)
def home_view():
    return "<h1>helllo</h1>"
    
@app.post("/")
def home_detail_view():
    return {"hello":"world"}