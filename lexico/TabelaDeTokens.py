'''
Created on 30 de ago de 2016

@author: Raul
'''
#-*-coding:utf-8-*-
from lexico.Lexema import *


class TabelaDeTokens(object):
    #Classe responsavel por guardar na ordem correta os tokens que foram encontrados no texto
    __podeImprimir = True
    
    def __init__(self):
        self.__tabela=[]
    
    def getTabela(self):
        return self.__tabela
    
    def addSimbolo(self,lexema):
        self.__tabela.append(lexema)
    
    def setPodeImprimir(self):
        self.__podeImprimir=False
             
    def imprimir(self):
        if(self.__podeImprimir):
            for i in self.__tabela:
                print("|%s,%s, %s|"%(i.token.tipo,i.lexema,i.linha))
        else:
            print("")
    
    
    
            
        