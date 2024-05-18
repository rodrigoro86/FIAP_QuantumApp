from fastapi.responses import JSONResponse
from src.db.nosql.db_mongodb import DB_Cliente
from src.model.clienteModel import ClienteModel

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


    