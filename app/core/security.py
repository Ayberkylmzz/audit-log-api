from fastapi import Header, HTTPException

from app.core.config import API_KEY


def verify_api_key(x_api_key: str | None = Header(default=None)):
    if x_api_key is None or x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")
