'''
Created on 30 de ago de 2016

@author: Raul
'''
#-*-encoding:uft-8-*-
from Lex import *
from Tolken import*
if __name__ == '__main__':
    
    t0 = Tolken("IDENTIFICADOR",r"(\b[a-zA-Z])\w*")
    t1 = Tolken("IGUAL",r'=')
    t2 = Tolken("NUMERO",r"\d+\s|\d+$")
    
    lex = Lex()
    lex.addTolken(t0)
    lex.addTolken(t1)
    lex.addTolken(t2)
    
    lex.analiseLexica("""x2xx=2 s s s 
    3 2 456""").imprimirTabela()
    
    
    pass