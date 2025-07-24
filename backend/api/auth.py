from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.services.auth_service import login_to_match_trade

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
async def login(req: LoginRequest):
    token = login_to_match_trade(req.username, req.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"token": token}
