'''
Created on 25 de set de 2016

@author: Raul
'''

class Pilha(object):

    def __init__(self, varInicial):
        self.__pilha = []
    
    def push(self,elemento):
        self.__pilha.append(elemento)
        
    def pop(self):
        self.__pilha.remove(self.__pilha[0])
        