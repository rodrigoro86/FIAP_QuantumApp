from motor.motor_asyncio import AsyncIOMotorClient
from conf.config import settings, logger
from pymongo import ASCENDING
from pymongo.errors import DuplicateKeyError




class DB_Cliente:
    def __init__(self):
        client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING)
        self.db = client['cliente']

        self.collection_name = 'clientes'
        self.collection = self.db[self.collection_name ]

    @classmethod
    async def create(cls):
        self = cls()
        await self.setup()
        return self

    async def setup(self):
        # Verifica se a coleção existe, se não, cria a coleção e o índice
        existing_collections = await self.db.list_collection_names()
        if self.collection_name not in existing_collections:
            print(f'Coleção "{self.collection_name}" não existe. Criando coleção e índice...')
            await self.collection.create_index([('cpf', ASCENDING)], unique=True)
        else:
            print(f'Coleção "{self.collection_name}" já existe.')


    async def insert(self, cliente):
        logger.info(f"Inserindo cliente no banco de dados {cliente.nome}")
        
        cliente_dict = cliente.dict(by_alias=True)
        # Converter campos date para string
        cliente_dict['data_de_nascimento'] = cliente_dict['data_de_nascimento'].isoformat()
        if cliente_dict.get('dados_conjuge'):
            cliente_dict['dados_conjuge']['data_de_nascimento'] = cliente_dict['dados_conjuge']['data_de_nascimento'].isoformat()

        try: 
            return await self.collection.insert_one(cliente_dict)
        except DuplicateKeyError:
            logger.warning(f'Cliente com CPF {cliente.cpf} já cadastrado no banco de dados.')
            raise ValueError(f'Cliente com CPF {cliente.cpf} já cadastrado no banco de dados.')


    async def find_all(self):
        return self.db.clientes.find()

    async def find_one(self, data):
        return self.db.clientes.find_one(data)

    async def update_one(self, data):
        return await self.db.clientes.update_one(data)

    async def delete_one(self, data):
        return await self.db.clientes.delete_one(data)