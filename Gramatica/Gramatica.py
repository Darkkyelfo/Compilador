'''
Created on 18 de set de 2016

@author: Raul

'''

from Variavel import Variavel
#-*-encoding:utf-8 -*-
class Gramatica(object):
       #Classe respons�vel por representar uma gram�tica

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
        
    def getGrammar(self):
        return self.__grammar
    
    def addVariavel(self,var):
        self.__listaProducoes.append(var)
    
    #M�todo respons�vel por encontrar todos os First das produ��es da gram�tica.
    def encontrarFirsts(self):
        for var in self.__listaProducoes:
            self.__first(var)
    def encontrarFollows(self):
        for var in self.__listaProducoes:
            if(var==self.__listaProducoes[0]):
                var.follows.append("$")
            
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
                
                
    def getListaProducoes(self):
        return self.__listaProducoes      
                
                