'''
Created on 18 de set de 2016

@author: Raul
'''
#-*-encoding:utf-8-*-
from gramatica.SimboloVazio import SimboloVazio
class Variavel(object):

       #Classe respons�vel por representar uma vari�vel de uma gram�tica 


    def __init__(self, simbolo):
        self.simbolo = simbolo
        self.producao = [[]]
        self.firsts = []
        self.follows= None
        self.temVazio = False# tag pra indicar se a palavra fazia � gerada pela producao
        self.guardarFollow = []
    def addProducao(self,producao):
        self.producao = producao # producao � uma lista podendo conter variaveis ou terminais
        
        if(self.temVazio==False):
            for i in self.producao:
                for e in i:
                    if(isinstance(e, SimboloVazio)):
                        self.temVazio = True
                        return -1
        
    

        