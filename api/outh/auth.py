from fastapi import FastAPI, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from jose import JWTError, jwt
from datetime import datetime, timedelta
import os

app = FastAPI()

SECRET_KEY = "123456" 
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class User(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

def authenticate_user(username: str, password: str):
    # Lógica para autenticar o usuário
    return True

# Função para criar um token JWT
def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@app.post("/login", response_model=Token)
async def login(user: User):
    if not authenticate_user(user.username, user.password):
        raise HTTPException(status_code=401, detail="Nome de usuário ou senha incorretos")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}