from fastapi import APIRouter, Form, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from torgpt.app.database.db import SessionLocal
from torgpt.app.database.models.user import User
from typing import Optional
from torgpt.app.config import settings
import httpx  # For making async requests to your Ollama instance

# Initialize the router and templates
router = APIRouter()
templates = Jinja2Templates(directory="src/torgpt/app/templates")

# Ollama instance configuration (adjust the URL if needed)
OLLAMA_API_URL = settings.ollama_url

# Dependency to get the current user from the cookie
def get_current_user(request: Request) -> Optional[str]:
    return request.cookies.get("auth")

@router.get("/", response_class=HTMLResponse)
async def chat_page(request: Request, user: str = Depends(get_current_user)):
    if not user:
        return RedirectResponse(url="/auth/login", status_code=303)
    return templates.TemplateResponse("chat.html", {"request": request})

@router.post("/", response_class=HTMLResponse)
async def send_prompt(
    request: Request, 
    prompt: str = Form(...), 
    user: str = Depends(get_current_user)
):
    if not user:
        return RedirectResponse(url="/auth/login", status_code=303)

    # Send prompt to the Ollama API
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(OLLAMA_API_URL, json={"prompt": prompt})
            response_data = response.json()
            reply = response_data.get("response", "Error: No response received.")
        except httpx.HTTPError as e:
            reply = f"Error communicating with Ollama API: {str(e)}"

    # Render the chat page with the response
    return templates.TemplateResponse(
        "chat.html",
        {
            "request": request,
            "response": reply,
        },
    )
