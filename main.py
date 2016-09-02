'''
Created on 30 de ago de 2016

@author: Raul
'''
#-*-encoding:uft-8-*-
from Lex import *
from Token import*
if __name__ == '__main__':
    
    #A ordem com se adiciona os tokens importa
    #pois,dependendo da expressão regular é possivel que trechos 
    #sejam igualmente reconhecido sendo que o lexema será catalogado
    #no tipo do tolken que possuir a exp regular que primeiro o reconhecer
    #exemplo: se trocar a ordem de "COMENTARIO" e "IDENTIFICADOR"
    #a palavra "comentário" na string será colocada como "IDENTIFICADOR"
    
    t0 = Token("COMENTARIO",r"#(\w|#|\s)*",True)
    t1 = Token("IGUAL",r'=')
    t2 = Token("NUMERO",r"\d+\s|\d+$")
    t3 = Token("IDENTIFICADOR",r"(\b([a-zA-Z]))\w*")
    
    lex = Lex()
    lex.addTolken(t0)
    lex.addTolken(t1)
    lex.addTolken(t2)
    lex.addTolken(t3)
    
    lex.analiseLexica("""x2xx=2 so si sa 
    #comentario aaaaa
    3 2 456""").imprimirTabela()
    
    
    pass