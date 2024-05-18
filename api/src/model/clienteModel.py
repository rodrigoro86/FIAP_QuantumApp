from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field, validator
from datetime import date
from enum import Enum
import re

class SexoEnum(str, Enum):
    masculino = 'Masculino'
    feminino = 'Feminino'
    nao_informado = 'Não Informado'

class TipoContaEnum(str, Enum):
    corrente = 'Corrente'
    poupanca = 'Poupança'
    salario = 'Salário'

class Contato(BaseModel):
    telefone_residencial: Optional[str] = Field(None, description="Telefone residencial do cliente", example="123456789")
    celular: str = Field(..., description="Celular do cliente", example="987654321")
    email: Optional[EmailStr] = Field(None, description="Email do cliente", example="cliente@example.com")

class Endereco(BaseModel):
    rua: str = Field(..., description="Rua do endereço do cliente", example="Rua Exemplo")
    numero: str = Field(..., description="Número do endereço do cliente", example="123")
    complemento: Optional[str] = Field(None, description="Complemento do endereço do cliente", example="Apto 101")
    bairro: str = Field(..., description="Bairro do endereço do cliente", example="Centro")
    cidade: str = Field(..., description="Cidade do endereço do cliente", example="São Paulo")
    estado: str = Field(..., description="Estado do endereço do cliente", example="SP")
    cep: str = Field(..., description="CEP do endereço do cliente", example="01000-000")

    @validator('cep')
    def validar_cep(cls, v):
        if not re.match(r'^\d{5}-\d{3}$', v):
            raise ValueError('CEP inválido. O formato deve ser 00000-000.')
        return v

class Conjuge(BaseModel):
    nome: str = Field(..., description="Nome do cônjuge", example="Maria")
    sobrenome: str = Field(..., description="Sobrenome do cônjuge", example="Silva")
    cpf: str = Field(..., description="CPF do cônjuge", example="987.654.321-00")
    rg: str = Field(..., description="RG do cônjuge", example="SP-98.765.432")
    data_de_nascimento: date = Field(..., description="Data de nascimento do cônjuge", example="1982-02-02")

    @validator('cpf')
    def validar_cpf(cls, v):
        if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', v):
            raise ValueError('CPF inválido. O formato deve ser 000.000.000-00.')
        return v

    @validator('rg')
    def validar_rg(cls, v):
        if not re.match(r'^[a-zA-Z]{2}-\d{2}\.\d{3}\.\d{3}$', v):
            raise ValueError('RG inválido. O formato deve ser XX-00.000.000.')
        return v

class ClienteModel(BaseModel):
    foto: bytes = Field(..., description="Foto do cliente em formato binário", example=b'binarydata')
    assinatura_eletronica: bytes = Field(..., description="Assinatura eletrônica do cliente em formato binário", example=b'binarydata')
    contatos: Contato = Field(..., description="Informações dos contatos do cliente", example={"telefone_residencial": "123456789", "celular": "987654321", "email": "cliente@example.com"})
    numero_conta: str = Field(..., alias='nº da conta', description="Número da conta do cliente", example="456789")
    tipo_conta: TipoContaEnum = Field(..., alias='tipo de conta', description="Tipo de conta do cliente", example="corrente")
    nome: str = Field(..., description="Nome do cliente", example="João")
    sobrenome: str = Field(..., description="Sobrenome do cliente", example="Silva")
    nome_social: Optional[str] = Field(None, description="Nome social do cliente", example="Joana")
    cpf: str = Field(..., description="CPF do cliente", example="123.456.789-00")
    rg: str = Field(..., description="RG do cliente", example="MG-12.345.678")
    data_de_nascimento: date = Field(..., description="Data de nascimento do cliente", example="1980-01-01")
    sexo: SexoEnum = Field(..., description="Sexo do cliente", example="Masculino")
    endereco_completo: Endereco = Field(..., description="Endereço completo do cliente")
    nacionalidade: str = Field(..., description="Nacionalidade do cliente", example="Brasileira")
    certidao_estado_civil: str = Field(..., description="Certidão de estado civil do cliente", example="123456")
    dados_conjuge: Optional[Conjuge] = Field(None, description="Dados do cônjuge do cliente", example={"nome": "Maria", "sobrenome": "Silva", "cpf": "987.654.321-00", "rg": "SP-98.765.432", "data_de_nascimento": "1982-02-02"})


    @validator('cpf')
    def validar_cpf(cls, v):
        if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', v):
            raise ValueError('CPF inválido. O formato deve ser 000.000.000-00.')
        return v

    @validator('rg')
    def validar_rg(cls, v):
        if not re.match(r'^[a-zA-Z]{2}-\d{2}\.\d{3}\.\d{3}$', v):
            raise ValueError('RG inválido. O formato deve ser XX-00.000.000.')
        return v

    class Config:
        allow_population_by_field_name = True
