'''
Created on 30 de ago de 2016

@author: Raul
'''
#-*-coding:utf-8-*-
from Lexema import *
class TabelaDeSimbolos(object):
    __tabela = []
    def addSimbolo(self,lexema):
        self.__tabela.append(lexema)
            
    def imprimirTabela(self):
        for i in self.__tabela:
            print("|%s, %s, %s|"%(i.tolken.tipo,i.lexema,i.linha))
            
        