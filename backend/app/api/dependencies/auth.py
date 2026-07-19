from fastapi import Header, HTTPException
from typing import Tuple

async def get_current_user_and_role(x_demo_token: str = Header(default=None)) -> Tuple[str, str]:
    if not x_demo_token:
        raise HTTPException(status_code=401, detail="Unauthenticated user.")
        
    role = "operator"
    if x_demo_token == "token_supervisor": role = "supervisor"
    elif x_demo_token == "token_admin": role = "admin"
    elif x_demo_token == "token_ai": role = "ai"
    
    return x_demo_token, role
