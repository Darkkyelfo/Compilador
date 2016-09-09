'''
Created on 30 de ago de 2016
@author: Raul
'''
#-*-encoding:uft-8-*-
from Lex import *
from Token import*
if __name__ == '__main__':
    lex = Lex()
    #A ordem com se adiciona os tokens importa
    #pois,dependendo da expressão regular é possivel que trechos 
    #sejam igualmente reconhecido sendo que o lexema será catalogado
    #no tipo do tolken que possuir a exp regular que primeiro o reconhecer
    #exemplo: se trocar a ordem de "COMENTARIO" e "IDENTIFICADOR"
    #a palavra "comentário" na string será colocada como "IDENTIFICADOR"
    
    reservada = {'if':'IF','else':'ELSE','while':'WHILE','for':'FOR',
                 'break':'BREAK',"continue":"CONTINUE","def":"DEF"}
    
    separadores = {"\(":"LPAREN","\)":"RPAREN","\:":"DOISPONTOS","\,":"VIRGULA"}
    comparacoes = {"==":"IGUAL","<=":"MENOROUIGUAL",">=":"MAIOROUIGUAL"
                   ,">":"MAIORQUE","<":"MENORQUE"}
    operacoesMat = {"\+":"MAIS","-":"MENOS","\*\*":"POT","\*":"MULTI","/":"DIVI"}
    
    t0 = Token("COMENTARIO",r"#(\w|#|\s)*",True)
    t1 = Token("ATRIBUICAO",r'=')
    for i in reservada:#add as palavras reservadas
        ttemp = Token(reservada[i],r"%s"%i)
        lex.addTolken(ttemp)
    for i in separadores:
        ttemp = Token(separadores[i],r"%s"%i)
        lex.addTolken(ttemp)
    for i in comparacoes:
        ttemp = Token(comparacoes[i],r"%s"%i)
        lex.addTolken(ttemp)
    for i in operacoesMat:
        ttemp = Token(operacoesMat[i],r"%s"%i)
        lex.addTolken(ttemp)
    t2 = Token("STRING",r"(\"\w*\")|(\'\w*\')")
    t3 = Token("IDENTIFICADOR",r"(\b([a-zA-Z]))\w*")
    t4 = Token("NUMERO",r"\d+")
    t5 = Token("IDENTACAO",r"\s",True)
    
    lex.addTolken(t0)
    lex.addTolken(t1)
    lex.addTolken(t2)
    lex.addTolken(t3)
    lex.addTolken(t4)
    lex.addTolken(t5)
    
    lex.analiseLexica("""x2xx=2
    if(x2xx==3):
        print("oi")
    def func(a)
    #comentario aaaaa
    3 2 456""").imprimirTabela()