'''
Created on 30 de ago de 2016

@author: Raul
'''
#-*-encoding:utf-8-*-
import re
from TabelaSimbolos import TabelaDeSimbolos
from Lexema import *
from TolkenInvalidoError import *

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
                            linha = linha.replace(lexema.lexema," ")#Apaga o lexema encontrado da string
                    self.__houveTokenInvalido(linha,num)#detecta se na linha houve algum tolken ilegal
                    listaLex.sort(key=lambda x: x.posicao, reverse=False)#Organiza os tolkens na ordem que aparecem na lista 
                    for i in listaLex:#add os lexemas encontrados a tabela de símbolos
                        self.tSimbolos.addSimbolo(i)
            except(TypeError):
                print(u"Sua expressão regular não é precisa o suficiente")
            except (TolkenInvalidoError) as e:
                print(str(e))
            return self.tSimbolos
    
    #Função responsavel por detectar se existe algum token inválido(não definido)
    #na string. Para isso ela verifica se a linha é composta somente por " "
    #pois,sempre que umlexema é encontrado no pelo lex ele o remove da string. 
    def __houveTokenInvalido(self,linha,num):
        for i in linha:
            if(i!=" "):
                raise TolkenInvalidoError(u"Tolken Inválido:%s na linha:%s"%(i,num+1))
                break
            
            
        
        
        
        
        