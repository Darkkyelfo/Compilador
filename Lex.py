'''
Created on 30 de ago de 2016

@author: Raul
'''
#-*-encoding:utf-8-*-
import re
from TabelaSimbolos import TabelaDeSimbolos
from Lexema import *

class Lex(object):
    listaTolkens = []
    tSimbolos= TabelaDeSimbolos()
    __ignorar = []
    def addTolken(self,tolken):
        self.listaTolkens.append(tolken)
    
    def addIgnorar(self,tolken):
        self.__ignorar.append(tolken)
    
    def analiseLexica(self,codigo):
        if(len(self.listaTolkens)==0):
            print(u"Não existem tolkens definidos para sua linguagem")
        else:
            try:
                for num,linha in enumerate(codigo.split("\n")):#Percorre a string linha a linha
                    listaLex = []
                    for tolken in self.listaTolkens:
                        exp = re.compile(tolken.expRegular)#Recebe a expressão regular que vai ser procurada
                        for match in exp.finditer(linha):#Encontra as string que correspondem a expressão regular
                            posicao = match.start()#pega a posicao na linha do lexema encontrado
                            lexema = Lexema(match.group(),tolken,num+1,posicao)#cria o lexema
                            listaLex.append(lexema)#add os lexemas a lista
                    listaLex.sort(key=lambda x: x.posicao, reverse=False)#Organiza os tolkens na ordem que aparecem na lista 
                    for i in listaLex:#add os lexemas encontrados a tabela de símbolos
                        self.tSimbolos.addSimbolo(i)
            except(TypeError):
                print(u"Sua expressão regular não é precisa o suficiente")
            
            return self.tSimbolos
    
            
        
        
        
        
        