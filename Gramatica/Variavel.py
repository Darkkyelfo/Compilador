'''
Created on 18 de set de 2016

@author: Raul
'''
#-*-encoding:utf-8-*-
class Variavel(object):

       #Classe respons�vel por representar uma vari�vel de uma gram�tica 


    def __init__(self, simbolo):
        self.variavel = simbolo
        self.producao = [[]]
        self.firsts = []
        self.follows= None
        
    def addProducao(self,producao):
        self.producao = producao # producao � uma lista podendo conter variaveis ou terminais
        
    

        