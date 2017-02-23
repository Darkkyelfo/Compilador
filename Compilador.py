'''
Created on 21 de fev de 2017

@author: raul
'''
from gramatica.Gramatica import Gramatica
from lexico.Lex import Lex
from lexico.Token import Token
from sintatico.AnalisadorSintatico import AnalisadorSintatico
from sintatico.TabelaSintatica import TabelaSintatica
from semantico.AnalisadorSemantico import AnalisadorSemantico
from Tradutor import Tradutor3Enderecos,Impressor

class Compilador(object):


    def __init__(self):
        self.lex = Lex()
        #Recebe o arquivo contendo a gramática
        self.gramatica = Gramatica()
        self.gramatica.extrairDeArquivo("arquivos/GramaticaSeparada2.txt")
        #Recebe o arquivo contendo a tabela para a análise sintática
        tabelaSint = TabelaSintatica()
        tabelaSint.gerarTabelaArq("arquivos/tabelaGramatica3_2.csv")
        
        self.anaSintatico = AnalisadorSintatico(self.gramatica)
        self.anaSintatico.tabelaSintatica = tabelaSint
        
        self.traducao = ""
        self.impressor = []
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
            self.lex.addTolken(ttemp)
        for i in separadores:
            ttemp = Token(separadores[i],r"%s"%i)
            self.lex.addTolken(ttemp)
        for i in comparacoes:
            ttemp = Token(comparacoes[i],r"%s"%i)
            self.lex.addTolken(ttemp)
        for i in operacoesMat:
            ttemp = Token(operacoesMat[i],r"%s"%i)
            self.lex.addTolken(ttemp)
            
        t2 = Token("STRING",r"(\"\w*\")|(\'\w*\')")
        t3 = Token("funcId",r"(\b([a-zA-Z]))\w*\s*\(")#Identificador de funcao
        t4 = Token("id",r"(\b([a-zA-Z]))\w*")#Identificador de variáveis 
        t5 = Token("numero",r"\d+")
        t6 = Token("newline",r"\n+")#"." pega qualquer valor menos newline. "^" negação.
        t7 = Token("IDENTACAO",r"\s",True)
        
        self.lex.addTolken(t0)
        self.lex.addTolken(t1)
        self.lex.addTolken(t2)
        self.lex.addTolken(t3)
        self.lex.addTolken(t4)
        self.lex.addTolken(t5)
        self.lex.addTolken(t6)
        self.lex.addTolken(t7)
    
    def compilar(self,codigo):
        self.lex.analiseLexica(codigo)
        
        self.anaSintatico.analisarSintaxe(self.lex.tLexemas.getTabela(),1)
        anaSemantico  = AnalisadorSemantico()
        anaSemantico.analiseSemantica(self.lex.tLexemas.getTabela())
        
        tradutor = Tradutor3Enderecos(self.lex.tLexemas.getTabela())
        
        self.traducao = tradutor.converter()
        
        self.impressor = Impressor.vImprimir(self.lex.tLexemas.getTabela(),anaSemantico.escopo)
        

        