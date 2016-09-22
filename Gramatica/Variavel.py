'''
Created on 18 de set de 2016

@author: Raul
'''
#-*-encoding:utf-8-*-
from Gramatica import SimboloVazio
class Variavel(object):

       #Classe responsável por representar uma variável de uma gramática 


    def __init__(self, simbolo):
        self.variavel = simbolo
        self.producao = [[]]
        self.firsts = []
        self.follows= None
        self.temVazio = False# tag pra indicar se a palavra fazia é gerada pela producao
        self.guardarFollow = []
    def addProducao(self,producao):
        self.producao = producao # producao é uma lista podendo conter variaveis ou terminais
        
        if(self.temVazio==False):
            for i in self.producao:
                for e in i:
                    if(isinstance(e, SimboloVazio)):
                        self.temVazio = True
                        return -1
        
    

        