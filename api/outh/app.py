from fastapi import FastAPI, HTTPException, Request, Depends, JSONResponse
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
import requests
import os

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = "123456"  # Use uma chave secreta forte
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Não autorizado")
    except JWTError:
        raise HTTPException(status_code=401, detail="Não autorizado")
    return username

@app.post('/api/predictions')
async def get_weather(request: Request, current_user: str = Depends(get_current_user)):
    
    return JSONResponse(content={"message": "Hello, World!"})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
