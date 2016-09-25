'''
Created on 22 de set de 2016

@author: Raul
'''
from tabelaDeSimbolos.Identificador import Identificador


class TabelaDeSimbolos(object):
    #Armazena o estado dos identificadores
    #tipo(bool ou numerico), valor e a linha em que aparece
    def __init__(self,TabelaDeTokens,tipoProcurado):
        self.__tabela = []
        for indice,lexema in enumerate(TabelaDeTokens.getTabela()):
            if(lexema.token.tipo==tipoProcurado):
                tipo = None
                if(lexema.lexema.isnumeric()):
                    tipo="numero"
                elif(lexema.lexema=="True" or lexema.lexema=="False"):
                    tipo = "boleano"
                self.__addSimbolo(lexema, TabelaDeTokens.getTabela()[indice+2], tipo)
    
    def __addSimbolo(self,lexema,valor,tipo,contexto):
        for id in self.__tabela:
            if(id.nome == lexema.lexema and id.contexto==contexto):
                id.valor = valor
                id.tipo = tipo
                return 0
        id = Identificador(lexema,valor,tipo,contexto)
        self.__tabela.append(id)
                    
                
    
    
    
    
    
        
        