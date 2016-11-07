'''
Created on 7 de nov de 2016

@author: Raul
'''
# -*- coding:utf-8 -*-
from semantico.TabelaDeSimbolos import TabelaDeSimbolos
from semantico.Escopo import Escopo
from semantico.ErroSemantico import ErroSemantico

class AnalisadorSemantico(object):
    u'''
    Classe que é responsável por realizar a analise semântica
    '''
    tiposEscopos = ("if","else","while","def")#guarda os tipos de escopo
    dentroLaco = ("break","continue")#palavras chaves que só devem existir dentro do "while"

    def __init__(self):
        self.tabelaDeSimbolos = TabelaDeSimbolos()
        self.escopo = Escopo()
    
    def analiseSemantica(self,tabelaDeTokens):
        
        escopoAtual = self.escopo
        for lexema in tabelaDeTokens:
            if(lexema.token.tipo in self.tiposEscopos):#localiza os escopos
                filho = Escopo(escopoAtual,len(escopoAtual.escoposFilhos),lexema.token.tipo)
                escopoAtual.addFilho(filho)
                escopoAtual = filho
                
            elif(lexema.token.tipo == "}"):
                escopoAtual = escopoAtual.escopoPai
                
            elif(lexema.token.tipo in self.dentroLaco):#se o "break" ou "continue" aparecer fora do laço lance uma exceção 
                escopoT = escopoAtual
                dentroDoLaco = False
                while(escopoT.tipo != "main"):#verifica os escopos pai. Caso o break esteja em um if e esse if esteja em um laço por exemplo 
                    if(escopoAtual.tipo == self.tiposEscopos[2]):
                        dentroDoLaco = True
                        break
                    escopoT = escopoAtual.escopoPai
                if(dentroDoLaco==False):
                    raise ErroSemantico(u"Erro semântico: '%s' deve estar dentro de um laço de repetição"%lexema.token.tipo)
        
            elif(lexema.token.tipo == "id" or lexema.token.tipo == "funcId"):
                print("add a tabela de Simbolos")
                    
                
            
            
            
            
            
        
        
        
        