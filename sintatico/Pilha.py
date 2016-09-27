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
        del self.__pilha[-1]
        self.__tamanho-=1 
        
    def topo(self):
        return self.__pilha[-1]
    
    def getTamanho(self):
        return self.__tamanho
    
    def imprimir(self):
        for i in range(len(self.__pilha),0,-1):
            print(self.__pilha[i-1].simbolo)
             