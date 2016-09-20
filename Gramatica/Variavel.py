'''
Created on 18 de set de 2016

@author: Raul
'''
#-*-encoding:utf-8-*-
class Variavel(object):

       #Classe responsável por representar uma variável de uma gramática 


    def __init__(self, simbolo):
        self.variavel = simbolo
        self.producao = [[]]
        self.firsts = []
        self.follows= None
        
    def addProducao(self,producao):
        self.producao = producao # producao é uma lista podendo conter variaveis ou terminais
        
    

        