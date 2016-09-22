'''
Created on 30 de ago de 2016
@author: Raul
'''
#-*-encoding:utf-8-*-
import re
from TabelaDeTokens import TabelaDeTokens
from Lexema import *
from TokenInvalidoError import *

class Lex(object):
    listaTokens = []
    tSimbolos= TabelaDeTokens()
    __achados=[]#armazena as posições dos lexemas encontrados
    def addTolken(self,tolken):
        self.listaTokens.append(tolken)
     
    def analiseLexica(self,codigo):
        if(len(self.listaTokens)==0):
            print(u"Não existem tolkens definidos para sua linguagem")
        else:
            try:
                for num,linha in enumerate(codigo.split("\n")):#Percorre a string linha a linha
                    listaLex = []
                    copiaLinha = ""+linha
                    for token in self.listaTokens:
                        exp = re.compile(token.expRegular)#Recebe a expressão regular que vai ser procurada
                        for match in exp.finditer(linha):#Encontra as string que correspondem a expressão regular
                            posicao = match.start()#pega a posicao na linha do lexema encontrado
                            if(posicao not in self.__achados):#Se não foi achado ainda
                                if(token.ignorar==False):#caso o token seja ignoravel( um comentário por exemplo)
                                    lexema = Lexema(match.group(),token,num+1,posicao)#cria o lexema
                                    listaLex.append(lexema)#add os lexemas a lista
                                self.__addAchados(posicao, len(match.group()))#add aos achados
                            copiaLinha = copiaLinha.replace(match.group(),"")#Apaga o lexema encontrado da string
                    self.__houveTokenInvalido(copiaLinha,num)#detecta se na linha houve algum token ilegal
                    listaLex.sort(key=lambda x: x.posicao, reverse=False)#Organiza os tolkens na ordem que aparecem na lista 
                    self.__apagarAchados()
                    for i in listaLex:#add os lexemas encontrados a tabela de símbolos
                        self.tSimbolos.addSimbolo(i)
            except (TokenInvalidoError) as e:
                self.tSimbolos.setPodeImprimir()#impede que os simbolos encontrados sejam impressos
                print(str(e))
            return self.tSimbolos
    
    #Função responsavel por detectar se existe algum token inválido(não definido)
    #na string. Para isso ela verifica se a linha é composta somente por " "
    #pois,sempre que umlexema é encontrado no pelo lex ele o remove da string. 
    def __houveTokenInvalido(self,linha,num):
        if(len(linha)>0):
            raise TokenInvalidoError(u"Tolken Inválido:%s na linha:%s"%(linha,num+1))
    
    #Sempre que o lex encontrar uma expressão que corresponda a expressão regular
    #Sua posição será adiciona aqui assim se outro expressão regular também
    #concidir a expressão não será adicionada novamente a tabela de tokens
    #Em suma evita a repetição de tokens caso as expressões regulares não sejam
    #"Precisas" o suficiente 
    def __addAchados(self,comeco,tamanho):
        for i in range(comeco,comeco+tamanho):
            self.__achados.append(i)
    
    def __apagarAchados(self):
        self.__achados=[]