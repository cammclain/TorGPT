from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import RedirectResponse
from torgpt.app.database.db import get_user_by_username

router = APIRouter()

@router.get("/login")
async def login_page():
    return {"template": "login.html"}

@router.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    user = get_user_by_username(username)
    if user and user.verify_password(password):
        response = RedirectResponse(url="/chat", status_code=303)
        response.set_cookie(key="auth", value=user.username)
        return response
    return {"error": "Invalid credentials"}
