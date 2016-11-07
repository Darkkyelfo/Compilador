'''
Created on 22 de set de 2016

@author: Raul
'''

class Identificador(object):
    # Classe responsavel por representar o token especial "id"
    # Armazena seu nome, tipo e valor 

    def __init__(self,lexema,valor,tipo,escopo):
        self.lexema = lexema
        self.valor = valor
        self.tipo = tipo
        self.escopo = escopo
    
        
        