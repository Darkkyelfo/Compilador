'''
Created on 18 de set de 2016

@author: Raul

'''

from gramatica.Sifrao import *
from gramatica.SimboloVazio import SimboloVazio
from gramatica.Terminal import *
from gramatica.Variavel import Variavel


#-*-encoding:utf-8 -*-
class Gramatica(object):
       #Classe respons�vel por representar uma gram�tica
       #Essa Classe ainda não está terminada 
    __modeloGramatica = u""" A gram�tica deve ser LL(1), onde
         Variaveis come�am com < e terminam com > e terminais ficam entre aspas simples:''
        Exemplo de gram�tica:
            <E> = <T><R>
            <R> = '+'<T><R>|e
            <Z> = '*'<F><Z>|e
            <F> = '('<E>')'|'id'
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
        self.__listaProducoes[0].follows.append(Sifrao())#add o sifrao ao primeiro elemento
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
                                       
                
                