'''
Created on 30 de ago de 2016

@author: Raul
'''
#-*-encoding:utf-8-*-
import re
from TabelaSimbolos import TabelaDeSimbolos
from Lexema import *
from TokenInvalidoError import *

class Lex(object):
    listaTokens = []
    tSimbolos= TabelaDeSimbolos()
    __reservadas =[]
    def addTolken(self,tolken):
        self.listaTokens.append(tolken)
     
    def analiseLexica(self,codigo):
        if(len(self.listaTokens)==0):
            print(u"Não existem tolkens definidos para sua linguagem")
        else:
            try:
                for num,linha in enumerate(codigo.split("\n")):#Percorre a string linha a linha
                    listaLex = []
                    for token in self.listaTokens:
                        exp = re.compile(token.expRegular)#Recebe a expressão regular que vai ser procurada
                        for match in exp.finditer(linha):#Encontra as string que correspondem a expressão regular
                            if(token.ignorar==False):#caso o token seja ignoravel( um comentário por exemplo)
                                posicao = match.start()#pega a posicao na linha do lexema encontrado
                                lexema = Lexema(match.group(),token,num+1,posicao)#cria o lexema
                                listaLex.append(lexema)#add os lexemas a lista
                            linha = linha.replace(match.group()," ")#Apaga o lexema encontrado da string
                    self.__houveTokenInvalido(linha,num)#detecta se na linha houve algum token ilegal
                    listaLex.sort(key=lambda x: x.posicao, reverse=False)#Organiza os tolkens na ordem que aparecem na lista 
                    for i in listaLex:#add os lexemas encontrados a tabela de símbolos
                        self.tSimbolos.addSimbolo(i)
            except(TypeError):
                print(u"Sua expressão regular não é precisa o suficiente")
            except (TokenInvalidoError) as e:
                self.tSimbolos.setPodeImprimir()#impede que os simbolos encontrados sejam impressos
                print(str(e))
            return self.tSimbolos
    
    #Função responsavel por detectar se existe algum token inválido(não definido)
    #na string. Para isso ela verifica se a linha é composta somente por " "
    #pois,sempre que umlexema é encontrado no pelo lex ele o remove da string. 
    def __houveTokenInvalido(self,linha,num):
        for i in linha:
            if(i!=" "):
                raise TokenInvalidoError(u"Tolken Inválido:%s na linha:%s"%(i,num+1))
            
            
            
        
        
        
        
        