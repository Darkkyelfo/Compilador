'''
Created on 22 de set de 2016

@author: Raul
'''
# -*- coding:utf-8 -*-
from semantico import ErroSemantico
class TabelaDeSimbolos(object):
    #Armazena o estado dos identificadores
    #tipo(bool ou numerico), valor,linha em que aparece e o escopo em que aparece
    #É utilizada na analise semantica
    def __init__(self):
        self.__tabela = {}
        self.vazia = True
    
    def addIdentificador(self,id):
        self.__tabela[id.lexema.lexema]=id
    
    def getIdentificador(self,nome):
        return self.__tabela[nome]

                    
                
    
    
    
    
    
        
        