from fastapi.responses import JSONResponse
from src.db.nosql.db_mongodb import DB_Cliente
from src.model.clienteModel import ClienteModel

from src.security.security import HashedPassword, pwd_context, verify_password
from conf.config import logger

from fastapi import(
    APIRouter,
)

router = APIRouter()
@router.post("/")
async def get_client():
    
    return JSONResponse(content={"message": "Hello World"})

@router.post("/cadastra_cliente")
async def cadastra_cliente(cliente: ClienteModel):
    db = await DB_Cliente.create()

    try:
        await db.insert(cliente)
        return JSONResponse(content={"message": "Cliente cadastrado com sucesso"})
    
    except ValueError as e:
    
        return JSONResponse(content={"message": str(e)}, status_code=400)


@router.post("/teste_hash")
async def teste_hash(password:str):
    logger.info(password)

    logger.info(verify_password(password, "$2b$12$YHJ.S7mlN.1ccd3lgITi2er/0eq9RcLRTh8GPbeG/BJ3k9Yb/JuZm"))
    return pwd_context.hash(password)