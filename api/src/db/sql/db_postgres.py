from sqlmodel import create_engine
from conf.config import settings   


engine = create_engine(
    settings.POSTGRES_URI, 
    echo=False,
    connect_args={},
)