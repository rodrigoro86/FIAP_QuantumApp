from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from src.api.router import api_router
from conf.config import settings, logger

import aiofiles


app = FastAPI(title='API QuantunApp')

app.include_router(api_router)
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    import uvicorn

    logger.info("Iniciando a aplicação QuantunApp")
    uvicorn.run(
        "main:app",
        reload=True,
        host="0.0.0.0", 
        port=8000
    )