'''
Created on 22 de set de 2016

@author: Raul
'''
from lexico.Lexema import Lexema


class Identificador(object):
    # Classe responsavel por representar o token especial "id"
    # Armazena seu nome, tipo e valor 

    def __init__(self,lexema,valor,tipo,contexto):
        self.nome = lexema.lexema
        self.linha = lexema.linha
        self.valor = valor
        self.tipo = tipo
        self.contexto = contexto
        
        