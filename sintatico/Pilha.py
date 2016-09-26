'''
Created on 25 de set de 2016

@author: Raul
'''

class Pilha(object):

    def __init__(self, varInicial):
        self.__pilha = [varInicial]
        self.__tamanho = 1
    
    def push(self,elemento):
        self.__pilha.append(elemento)
        self.__tamanho+=1 
        
    def pop(self):
        self.__pilha.remove(self.__pilha[-1])
        self.__tamanho-=1 
        
    def top(self):
        return self.__pilha[-1]
    
    def getTamanho(self):
        return self.__tamanho
        