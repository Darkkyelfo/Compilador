'''
Created on 30 de ago de 2016
@author: Raul
'''
#-*-encoding:uft-8-*-
from gramatica.Gramatica import Gramatica
from lexico.Lex import Lex
from lexico.Token import Token
from sintatico.AnalisadorSintatico import AnalisadorSintatico
from sintatico.TabelaSintatica import TabelaSintatica
from semantico.AnalisadorSemantico import AnalisadorSemantico
from semantico.ErroSemantico import ErroSemantico
from Tradutor import Tradutor3Enderecos
if __name__ == '__main__':
    lex = Lex()
    #A ordem com se adiciona os tokens importa
    #pois,dependendo da expressão regular é possivel que trechos 
    #sejam igualmente reconhecido sendo que o lexema será catalogado
    #no tipo do tolken que possuir a exp regular que primeiro o reconhecer
    #exemplo: se trocar a ordem de "COMENTARIO" e "IDENTIFICADOR"
    #a palavra "comentário" na string será colocada como "IDENTIFICADOR"
    
    reservada = {'if':'if','else':'else','while':'while',
                 'break':'break',"continue":"continue","def":"def","True":"True","False":"False",
                 "return":"return"}
    
    separadores = {"\(":"(","\)":")","\,":",","\}":"}","\{":"{"}
    comparacoes = {"==":"==","<=":"<=",">=":">="
                   ,">":">","<":"<","!=":"!="}
    operacoesMat = {"\+":"+","-":"-","\*":"*","/":"/"}
    
    t0 = Token("COMENTARIO",r"#(\w|#|\s)*",True)
    t1 = Token("=",r'=')
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
    t3 = Token("funcId",r"(\b([a-zA-Z]))\w*\s*\(")#Identificador de funcao
    t4 = Token("id",r"(\b([a-zA-Z]))\w*")#Identificador de variáveis 
    t5 = Token("numero",r"\d+")
    t6 = Token("newline",r"^.")#"." pega qualquer valor menos newline. "^" negação.
    t7 = Token("IDENTACAO",r"\s",True)
    
    lex.addTolken(t0)
    lex.addTolken(t1)
    lex.addTolken(t2)
    lex.addTolken(t3)
    lex.addTolken(t4)
    lex.addTolken(t5)
    lex.addTolken(t6)
    lex.addTolken(t7)

#imprime o resultado 
lex.tLexemas.imprimir()

#Recebe o arquivo contendo a gramática
gramatica = Gramatica()
gramatica.extrairDeArquivo("arquivos/GramaticaSeparada2.txt")

#Recebe o arquivo contendo a tabela para a análise sintática
tabelaSint = TabelaSintatica()
tabelaSint.gerarTabelaArq("arquivos/tabelaGramatica3_2.csv")

#tabelaSint.imprimir()
#print(tabelaSint.matriz[0])
#print(tabelaSint.linhas)
#print(tabelaSint.colunas)
#ssss
#Criando o analisador sintático
anaSintatico = AnalisadorSintatico(gramatica)
anaSintatico.tabelaSintatica = tabelaSint

#TESTANDO
lex.analiseLexica("""
    u=2
    t=5
    while(t>3){
        r=2+5*3
        b=2
        if(r>1){
            o=b+5
            t=3
        }else{
            y=r
            t=4
        }
        x=3
    }
    if(r>1){
        t=2
    }
    """
).imprimir()
if(anaSintatico.analisarSintaxe(lex.tLexemas.getTabela(),1)):
    print("Análise sintática realizada com sucesso")
    anaSemantico  = AnalisadorSemantico()
    try:
        anaSemantico.analiseSemantica(lex.tLexemas.getTabela())
        print("Análise semântica realizada com sucesso")
        tradutor = Tradutor3Enderecos(lex.tLexemas.getTabela())
        tradutor.converter()
    except(ErroSemantico) as e:
        print(str(e))
#anaSintatico.imprimirGramatica()    
