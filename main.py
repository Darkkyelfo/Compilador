'''
Created on 30 de ago de 2016
@author: Raul
'''
#-*-encoding:uft-8-*-
from gramatica.Gramatica import Gramatica
from gramatica.SimboloVazio import SimboloVazio
from gramatica.Terminal import Terminal
from gramatica.Variavel import Variavel
from lexico.Lex import Lex
from lexico.Token import Token
from sintatico.AnalisadorSintatico import AnalisadorSintatico
from sintatico.TabelaSintatica import TabelaSintatica
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
                   ,">":">","<":"<"}
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
    t3 = Token("FuncId",r"(\b([a-zA-Z]))\w*\s*\(")#Identificador de funcao
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
    lex.analiseLexica("""
    while(x>2){
        if(r>3){
            a=2*8
            b=4
        }
    }
    """
)
#add o vazio ao final da saída do analisador léxico
#vazioLexema = Lexema("vazio",Token("e",r""),-1,-1)
#lex.tLexemas.addSimbolo(vazioLexema)
#imprime o resultado 
lex.tLexemas.imprimirTabela()
# As partes a seguir são referentes a gramática
#VARIAVEIS
STATE = Variavel("STATE")
ATRIBUICAO = Variavel("ATRIBUICAO")
IF = Variavel("IF")
ELSE = Variavel("ELSE")
WHILE = Variavel("WHILE")
DEF = Variavel("DEF")
RETORNO = Variavel("RETORNO")
VALORES = Variavel("VALORES")
PARAMETROS = Variavel("PARAMETROS")
VIRGULA = Variavel("VIRGULA")
FUNCTIONCALL = Variavel("FUNCTIONCALL")
EXPRESSAO_ARITMETICA = Variavel("EXPRESSAO_ARITMETICA")
OPERACOES_ARITMETICAS = Variavel("OPERACOES_ARITMETICAS")
EXPRESSAO_LOGICA = Variavel("EXPRESSAO_LOGICA")
OPERADOR_LOGICO = Variavel("OPERADOR_LOGICO")
NEWLINES = Variavel("NEWLINES")
NEWLINE_SEQ = Variavel("NEWLINE_SEQ")
#Terminais
    #Reservadas
tIf = Terminal("if")
tElse = Terminal("else")
tWhile = Terminal("while")
tBreak = Terminal("break")
tContinue = Terminal("continue")
tDef = Terminal("def")
tTrue = Terminal("True")
tFalse = Terminal("False")
tRetorno = Terminal("return")
tNumero = Terminal("numero")
tFuncId = Terminal("FuncId")
    #Separadores
tPabrir = Terminal("(")
tPfechar = Terminal(")")
tVirgula = Terminal(",")
tChavesAbrir = Terminal("{")
tChavesFechar = Terminal("}")
    #Comparadores
tIgual = Terminal("==")
tDiferente = Terminal("!=")
tMaior = Terminal(">")
tMenor = Terminal("<")
tMaiorOr = Terminal(">=")
tMenorOr = Terminal("<=")
    #Operadores Matematicos
tMais = Terminal("+")
tMenos = Terminal("-")
tVezes = Terminal("*")
tDiv = Terminal("/") 
    #Identificador 
tId = Terminal("id")
    #newline
tNewline = Terminal("newline")
    #atribuicao
tAtribuicao = Terminal("=")
vazio = SimboloVazio()
#Producoes
pState = [[IF,STATE],[WHILE,STATE],[ATRIBUICAO,STATE],[DEF,STATE],[FUNCTIONCALL,STATE]
          , [RETORNO],[tBreak,NEWLINES],[tContinue,NEWLINES],[NEWLINES,STATE],
          [tNumero,OPERACOES_ARITMETICAS,NEWLINES,STATE],[vazio]]
pAtribuicao = [[tId,tAtribuicao,EXPRESSAO_ARITMETICA,NEWLINES]]
pIf = [[tIf,tPabrir,EXPRESSAO_LOGICA,tPfechar,tChavesAbrir,NEWLINES,STATE,tChavesFechar,ELSE]]
pElse = [[tElse,tChavesAbrir,NEWLINES,STATE,tChavesFechar,],[vazio]]
pWhile = [[tWhile,tPabrir,EXPRESSAO_LOGICA,tPfechar,tChavesAbrir,NEWLINES,STATE,tChavesFechar]]
pDef = [[tDef,tFuncId,tPabrir,PARAMETROS,tPfechar,tChavesAbrir,NEWLINES,STATE,tChavesFechar]]
pRetorno = [[tRetorno,VALORES]]
pValores = [[tId],[tTrue],[tFalse],[tNumero]]
pParametros = [[tId,VIRGULA],[vazio]]
pVirgula = [[tVirgula,tId,VIRGULA],[vazio]]
pFunctionCall = [[tFuncId,tPabrir,PARAMETROS,tPfechar,NEWLINES]]
pExp_ARI = [[tId,OPERACOES_ARITMETICAS],[tNumero,OPERACOES_ARITMETICAS]]
pOp_ARI =[[tMais,EXPRESSAO_ARITMETICA],[tMenos,EXPRESSAO_ARITMETICA],[tVezes,EXPRESSAO_ARITMETICA]
          ,[tDiv,EXPRESSAO_ARITMETICA],[vazio]]
pExpLogica = [[tTrue],[tFalse],[EXPRESSAO_ARITMETICA,OPERADOR_LOGICO]]
pOpLogico = [[tIgual,EXPRESSAO_ARITMETICA],[tMaior,EXPRESSAO_ARITMETICA],[tMenor,EXPRESSAO_ARITMETICA]
          ,[tMaiorOr,EXPRESSAO_ARITMETICA],[tMenorOr,EXPRESSAO_ARITMETICA],[tDiferente,EXPRESSAO_ARITMETICA]]
pNewlines = [[tNewline,NEWLINE_SEQ]]
pNewlineSeq = [[NEWLINES],[vazio]]
#Adiciona as produções as variaves 
STATE.addProducao(pState)
ATRIBUICAO.addProducao(pAtribuicao)
IF.addProducao(pIf)
ELSE.addProducao(pElse)
WHILE.addProducao(pWhile)
DEF.addProducao(pDef)
RETORNO.addProducao(pRetorno)
VALORES.addProducao(pValores)
PARAMETROS.addProducao(pParametros)
VIRGULA.addProducao(pVirgula)
FUNCTIONCALL.addProducao(pFunctionCall)
EXPRESSAO_ARITMETICA.addProducao(pExp_ARI)
OPERACOES_ARITMETICAS.addProducao(pOp_ARI)
EXPRESSAO_LOGICA.addProducao(pExpLogica)
OPERADOR_LOGICO.addProducao(pOpLogico)
NEWLINES.addProducao(pNewlines)
NEWLINE_SEQ.addProducao(pNewlineSeq)
#Cria a gramática 
gramatica = Gramatica()
gramatica.addVariavel(STATE)
gramatica.addVariavel(ATRIBUICAO)
gramatica.addVariavel(IF)
gramatica.addVariavel(ELSE)
gramatica.addVariavel(WHILE)
gramatica.addVariavel(DEF)
gramatica.addVariavel(RETORNO)
gramatica.addVariavel(VALORES)
gramatica.addVariavel(PARAMETROS)
gramatica.addVariavel(VIRGULA)
gramatica.addVariavel(FUNCTIONCALL)
gramatica.addVariavel(EXPRESSAO_ARITMETICA)
gramatica.addVariavel(OPERACOES_ARITMETICAS)
gramatica.addVariavel(EXPRESSAO_LOGICA)
gramatica.addVariavel(OPERADOR_LOGICO)
gramatica.addVariavel(NEWLINES)
gramatica.addVariavel(NEWLINE_SEQ)

#Análise Sintática
print("\n")
tabelaSint = TabelaSintatica()
tabelaSint.gerarTabelaArq("arquivos/tabelaGramatica3_2.csv")

#tabelaSint.imprimir()
#print(tabelaSint.matriz[0])
#print(tabelaSint.linhas)
#print(tabelaSint.colunas)

#Criando o analisador sintático
anaSintatico = AnalisadorSintatico(gramatica)
anaSintatico.tabelaSintatica = tabelaSint
if(anaSintatico.analisarSintaxe(lex.tLexemas.getTabela(),1)):
    print("Análise sintática realizada com sucesso")
#anaSintatico.imprimirGramatica()    
