#CONTEM OS MODELOS QUE REPRESENTAM AS ENTIDADES DO BANCO
#BOOK REPRESENTA A ENTIDADE BOOK
#uuid4() GERA UM ID UNICO PARA CADA LIVRO, ele é usado como chave primária para identificar de forma única cada registro na tabela. Isso garante que cada livro tenha um identificador exclusivo, mesmo que outros atributos (como título ou autor) possam ser iguais entre diferentes livros.

from uuid import uuid4
from sqlalchemy import String, Text
from sqlalchemy.dialects.postgresql import UUID
from db import db

class Book(db.Model):
#indica que Book é um modelo gerenciado do SQLAlchemy
    __tablename__ = 'book'
#define o nome da tabela
id = db.Column(
    UUID(as_uuid= True), #vou usar o UUID
    primary_key= True, #chave primaria
    default= uuid4 #quando criar um novo livro, um UUID será gerado
)
title = db.Column(
    String(255), #recebe a string
    nullable= False #não pode ser nulo
)
author = db.Column(
    String(255), 
    nullable= False 
)
#title e author são obrigatorios
description = db.Column(
    Text, #recebe um texto
    nullable= False #não pode ser nulo
)
is_favorite = db.Column(
    db.Boolean, #recebe um booleano
    nullable= False, #não pode ser nulo
    default= False #por padrão, o livro não é favorito
)
is_reading = db.Column(
    db.Boolean, #recebe um booleano
    nullable= False, #não pode ser nulo
    default= False #por padrão, o livro não está em leitura
)

is_finished = db.Column(
    db.Boolean, #recebe um booleano
    nullable= False, #não pode ser nulo
    default= False #por padrão, o livro não está finalizado
)
#TRANSFORMANDO O MODELO EM UM DICIONARIO
"""
POR ISSO SERÁ CRIADO UM METODO PARA TRANSFORMAR O OBJETO BOOK EM UM DICIONARIO PYTHON
QUANDO OCORRER UMA CONSULTA AO NOSSO SISTEMA ELE REORNA UM OBJETO BOOK, ELE NÃO É SIMPLISMENTE UM DICT PYTHON.
O METODO AS_DICT() FUNCIONA COMO UMA CAMADA DE CONVERSÃO, SELECIONANDO APENAS O NECESSARIO PARA SER EXPOSTO PELA API E TRANSFORMANDO EM UM DICT,
ESTRUTURA QUE PODE SER FACILMENTE SERIALIZADA PARA JSON RESPOSTA HTTP.
"""

def as_dict(self):
    return{
        "id":str(self.id), #necessario conversão forçada
        "title": self.title,
        "autor": self.autor,
        "description": self.description,
        "is_favorite": self.is_favorite,
        "is_reading": self.is_reading,
        "is_finished": self.is_finished
    }

