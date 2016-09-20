'''
Created on 19 de set de 2016

@author: Raul
'''
from Gramatica import *
from Variavel import *
from Terminal import *
from SimboloVazio import *
#arquivo temporario criado para testar a gramatica
if __name__ == '__main__':
    
    v0 = Variavel("E")
    v1 = Variavel("E1")
    v2 = Variavel("T")
    v3 = Variavel("T1")
    v4 = Variavel("F")
    
    t0 = Terminal("+")
    t1 = SimboloVazio()
    t2 = Terminal("*")
    t3 = Terminal("(")
    t4 = Terminal(")")
    t5 = Terminal("id")
    
    p0 = [[v2,v1]]
    p1 = [[t0,v2,v1],[t1]]
    p2 = [[v4,v3]]
    p3 = [[t2,v4,v3],[t1]]
    p4 = [[t3,v0,t4],[t5]]
    
    v0.addProducao(p0)
    v1.addProducao(p1)
    v2.addProducao(p2)
    v3.addProducao(p3)
    v4.addProducao(p4)
    
    gramatica = Gramatica()
    
    gramatica.addVariavel(v0)
    gramatica.addVariavel(v1)
    gramatica.addVariavel(v2)
    gramatica.addVariavel(v3)
    gramatica.addVariavel(v4)
    
    gramatica.encontrarFirsts()
    
    for i in gramatica.getListaProducoes():
        print(i.variavel)
        for j in i.firsts:
            print(j.simbolo)
        print("\n")
            
    
    pass