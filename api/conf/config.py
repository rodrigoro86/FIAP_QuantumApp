import os

from dynaconf import Dynaconf
from loguru import logger 
from pathlib import Path
import sys


HERE = os.path.dirname(os.path.abspath(__file__))


settings = Dynaconf(
    envvar_prefix="MYAPP",     #Tudo que tiver QUANTUNAPP_ será considerado
    preload=[os.path.join(HERE, "default.toml")],   #Carrega o arquivo default.toml antes de qualquer outro
    settings_files=["settings.toml", ".secrets.toml"],  #Carrega os arquivos settings.toml e .secrets.toml
    environments=['development', 'production', 'testing'],   #Define os ambientes disponíveis
    env_switcher="MYAPP_MODE",   #Variável de ambiente que define o ambiente
    load_dotenv=False,   #Carrega as variáveis de ambiente do arquivo .env
)


DIR_LOG:str = Path('logs/log_api.log')

logger.remove()
logger.add(DIR_LOG, level="INFO", 
    retention="10 days",
    format="""<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>""")

logger.add(sys.stdout, level="DEBUG", colorize=True,
    format="""<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"""       
    )

logger.debug(settings.db.uri)