from __future__ import annotations
from fastapi import FastAPI, JSONResponse
from fastapi.responses import JSONResponse
from torgpt.app.routes import auth, chat

app = FastAPI(
    title="TorGPT",
    description="TorGPT API",
    version="1.0.0",
)

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])

@app.get("/", response_model=dict[str, str])
def home() -> JSONResponse:
    """
    Root endpoint that returns a welcome message.
    """
    return JSONResponse(content={"message": "Welcome to TorGPT!"})
