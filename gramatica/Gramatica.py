'''
Created on 18 de set de 2016

@author: Raul

'''


from gramatica.SimboloVazio import SimboloVazio
from gramatica.Terminal import Terminal
from gramatica.Variavel import Variavel


#-*-encoding:utf-8 -*-
class Gramatica(object):
       #Classe respons�vel por representar uma gram�tica
       #Essa Classe ainda não está terminada 
    __modeloGramatica = u""" A gram�tica deve ser LL(1), onde
         Variaveis estão em maisculo e os terminais não. As produções
         devem ser separadas por "->", deve haver um espaço " " entre os termos e simbolo
         Vazio é representado por "e"
         Exemplo:
         STATE -> continue NEWLINES
         STATE -> NEWLINES STATE
         STATE -> numero OPERACOES_ARITMETICAS NEWLINES STATE
         STATE -> e
         DEF -> def funcId ( PARAMETROS ) { NEWLINES STATE } 
         """
         
    def __init__(self):
        self.__listaProducoes=[]

    def modeloGramatica(self):
        return self.__modeloGramatica
    
    def addVariavel(self,var):
        self.__listaProducoes.append(var)
                
    def getListaProducoes(self):
        return self.__listaProducoes 
    
    def getPrimeiraVar(self):
        return self.__listaProducoes[0]
    
    #Esse método é responsável por ler o arquivo contendo uma gramática LL(1)
    #e extrair seus terminais e variáveis. Transforma o arquivo em "objeto"
    def extrairDeArquivo(self,arquivo):
        arq = open(arquivo,"r")#lê o arquivo contendo a gramática
        texto = arq.readlines()#Gera um lista onde cada elemento é uma linha do arquivo
        dicPalavras = self.__encontrarVarEterminais(texto)#Encontra todas as Variáveis e terminais da no arquivo da grámtica
        self.__associarProducoes(texto, dicPalavras)# Cria as relações entre as Variáveis e suas produções.
        self.__addVariaveisAGramatica(texto, dicPalavras)# Add as Variáveis para a gramática seguindo a ordem com que aparecem no arquivo
        
    #Função responsavel por extrair as variáveis do arquivo contendo a gramática
    def __encontrarVarEterminais(self,texto):
        dic = {}# dicionario contendo as variáveis
        for linha in texto:
            for elemento in linha.split(" "):
                try:
                    dic[elemento]
                except KeyError:#caso o elemento não exista ele é add ao dicionário
                    elemento = elemento.replace("\n","")
                    if(elemento.isupper()):#se for maiúsculo é variavel
                        var = Variavel(elemento)
                        dic[elemento] = var
                    elif(elemento !="->" and elemento!=""):#não adiciona o separador "->" nem string vazia
                        if(elemento=="e"):
                            ter = SimboloVazio()
                        else:
                            ter = Terminal(elemento)
                        dic[elemento] = ter
        return dic
    
    #Esse método é responsavel por add as produções as variaveis
    #Exemplo: E-> AB-, essa função fica responsavel por associar a produção "AB-" a "E"                
    def __associarProducoes(self,texto,dicPalavras):
        listaProd = []
        for linha in texto:
                elemento = linha.split("->")
                for prod in elemento[1].split(" "):
                    try:
                        listaProd.append(dicPalavras[prod.replace("\n","")])
                    except KeyError:
                        continue     
                for i in elemento[0].split(" "):
                    if(i.isupper()):
                        dicPalavras[i].addProducao(listaProd)
                        listaProd = []
                        
    #Método para adicionar variáveis para gramática apartir de um arquivo          
    def __addVariaveisAGramatica(self,texto,dicPalavras):
        for linha in texto:
            if(dicPalavras[linha.split(" ")[0]] not in self.__listaProducoes):
                self.addVariavel(dicPalavras[linha.split(" ")[0]])
             
             
    #M�todo respons�vel por encontrar todos os First das produ��es da gram�tica.
    def encontrarFirsts(self):
        for var in self.__listaProducoes:
            self.__first(var)
    def encontrarFollows(self):
        for var in self.__listaProducoes:
            if(var==self.__listaProducoes[0]):
                var.follows.append("$")
                
    #Funciona Parcialmente     
    def __first(self,var):
        for prod in var.producao:
            if(isinstance(prod[0], Variavel)):
                firsts = self.__first(prod[0])
                for i in firsts:
                    if(i not in var.firsts):
                        var.firsts.append(i)
            else:
                if(prod[0] not in var.firsts):
                    var.firsts.append(prod[0])
        return var.firsts
    #Não funciona        
    def __follow(self):
        #self.__listaProducoes[0].follows.append(Sifrao())#add o sifrao ao primeiro elemento
        for var in self.__listaProducoes:
            self.__avaliarTipoFollow(var)
            if(var.temVazio):
                backupProd = var.producao + [] 
                for i in var.producao:
                    if(var in var.producao):
                        i.remove(var)
                self.__avaliarTipoFollow(var)
                var.producao = backupProd  
    #Não funciona                         
    def __avaliarTipoFollow(self,var):
        for i in var:
            for producao in i:
                if(len(producao)>=3):
                    for i in producao.producao[2].firsts:
                        if(isinstance(i,SimboloVazio)==False and i not in producao.follows):
                            producao[1].follows.append(i)
                elif(len(producao)>=2):
                    if(var not in producao[1].guardarFollow):
                        producao[1].guardarFollow.append(var)     
                                       
                
                