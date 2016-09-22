'''
Created on 30 de ago de 2016

@author: Raul
'''
#-*-coding:utf-8-*-
from Lexema import *
class TabelaDeTokens(object):
    __tabela = []
    __podeImprimir = True
    def addSimbolo(self,lexema):
        self.__tabela.append(lexema)
    
    def setPodeImprimir(self):
        self.__podeImprimir=False
             
    def imprimirTabela(self):
        if(self.__podeImprimir):
            for i in self.__tabela:
                print("|%s,%s, %s|"%(i.tolken.tipo,i.lexema,i.linha))
        else:
            print("")
            
        