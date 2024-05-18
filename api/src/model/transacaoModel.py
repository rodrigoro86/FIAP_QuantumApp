from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class FTransacao(SQLModel, table=True):
    id_transacao: Optional[int] = Field(default=None, primary_key=True, description="Identificador único da transação")
    n_banco_pagador: str = Field(max_length=50, description="Número do banco do pagador")
    n_agencia_pagador: str = Field(max_length=20, description="Número da agência do pagador")
    n_conta_pagador: str = Field(max_length=20, description="Número da conta do pagador")
    cpfcnpj_pagador: str = Field(max_length=20, description="CPF ou CNPJ do pagador")
    chave_pix_pagador: str = Field(max_length=50, description="Chave PIX do pagador")
    n_banco_credor: str = Field(max_length=50, description="Número do banco do credor")
    n_agencia_credor: str = Field(max_length=20, description="Número da agência do credor")
    n_conta_credor: str = Field(max_length=20, nullable=True, description="Número da conta do credor")
    cpfcnpj_credor: str = Field(max_length=20, description="CPF ou CNPJ do credor")
    chave_pix_credor: str = Field(max_length=50, description="Chave PIX do credor")
    valor_transacao: float = Field(description="Valor da transação")
    data_transacao: datetime = Field(description="Data da transação")
    id_status_transacao: int = Field(description="Identificador do status da transação")
    id_tipo_transacao: int = Field(description="Identificador do tipo de transação")
