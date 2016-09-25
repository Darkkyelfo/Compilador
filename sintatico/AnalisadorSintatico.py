'''
Created on 25 de set de 2016

@author: Raul
'''
#encoding:utf-8
from gramatica.Gramatica import Gramatica
from sintatico.Pilha import Pilha
class AnalisadorSintatico(object):
    u'''
        Classe responsavel por representar o analisador sintático
        ela recebe a gramática e a tabela Sintática para poder funcionar
        -IDEIA: posteriormente ela deve receber somente a gramática e a apartir dela construir
        a tabela
    '''


    def __init__(self,gramatica):
        self.__gramatica = self.__seperarGramatica(gramatica)
        self.tabelaSintatica = []#Atributo que armazena a tabela sintática. Será trocado por private futuramente.
        self.__pilha = Pilha(gramatica.getPrimeiraVar())
    
    #Método responsavel por deixar a gramatica em um formata mais simples para
    #se indexar com a tabela
    def __seperarGramatica(self,gramaticaNaoSepada):
        gramaticaSeparada = []
        for var in gramaticaNaoSepada.getListaProducoes():
            for prod in var.producao:
                gramaticaSeparada.append(prod)
        return gramaticaSeparada 
    
    def imprimirGramatica(self):
        cont= 0
        for i in self.__gramatica:
            cont+=1
            print("%s."%cont , end="")
            for j in i:
                print(j.simbolo, end=" ")
            print("\n")    
        