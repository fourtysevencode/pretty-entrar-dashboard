import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))              
from fastapi import FastAPI, Request
from utils.assignment_extractor import extract_assignments
from fastapi.templating import Jinja2Templates
from fastapi .responses import HTMLResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://assignments.ronakbuilds.tech",
        "https://pretty-entrar-dashboard.onrender.com/"
    ],
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


templates = Jinja2Templates(directory="templates")

class login_info(BaseModel):
    username:str
    password:str

@app.get("/", response_class=HTMLResponse) # HTML response, not json
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html")

@app.post("/fetch-assignments")
async def fetch_assignments(login_creds: login_info):
    return extract_assignments(login_creds.username, login_creds.password)