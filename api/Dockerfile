# Use a imagem oficial do Python
FROM python:3.12

# Defina o diretório de trabalho
WORKDIR /app

# Copie o código FastAPI para o contêiner
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY requirements.txt .

# Exponha a porta 8000 para acesso externo
EXPOSE 8000

# Comando para iniciar o servidor FastAPI
CMD ["python", "main.py"]