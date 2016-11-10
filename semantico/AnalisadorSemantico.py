'''
Created on 7 de nov de 2016

@author: Raul
'''
# -*- coding:utf-8 -*-
from semantico.TabelaDeSimbolos import TabelaDeSimbolos
from semantico.Escopo import Escopo
from semantico.ErroSemantico import ErroSemantico
from semantico.Identificador import Identificador
from semantico.FuncId import FuncId

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
        indiceTabelaSimbolos=0
        tamanho = len(tabelaDeTokens)
        while(indiceTabelaSimbolos<tamanho):
            lexema=tabelaDeTokens[indiceTabelaSimbolos]
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
                    if(escopoT.tipo == self.tiposEscopos[2]):
                        dentroDoLaco = True
                        break
                    escopoT = escopoT.escopoPai
                if(dentroDoLaco==False):
                    raise ErroSemantico(u"Erro semântico: '%s' deve estar dentro de um laço de repetição"%lexema.token.tipo)
            #Esse "if" é responsavel por tratar todos os acontecimentos associados a um identificador de função
            elif(lexema.token.tipo == "funcId"):
                comeco = indiceTabelaSimbolos
                if(comeco-1>0):
                    #Vai add o identificador da função a tabela
                    if(escopoAtual.tipo=="def" and tabelaDeTokens[comeco-1].token.tipo=="def"):
                        parametros = 0
                        for lexemaAux in tabelaDeTokens[comeco+2:]:
                            indiceTabelaSimbolos+=1
                            if(lexemaAux.token.tipo=="id"):
                                parametros+=1
                            elif(lexemaAux.token.tipo=="numero"):
                                raise ErroSemantico(u"Erro semântico: declaração de funções ou procedimentos deve possuir somente variáveis")
                            elif(lexemaAux.token.tipo==")"):
                                break    
                        funcId = FuncId(lexema,0,None,escopoAtual,parametros)
                        self.tabelaDeSimbolos.addIdentificador(funcId)
                        
            #Esse "if" é responsavel por tratar todos os acontecimentos associados a uma variável  
            elif(lexema.token.tipo == "id"):
                comeco = indiceTabelaSimbolos
                if(tabelaDeTokens[comeco+1].token.tipo=="="):#quando ocorre uma atribuição
                    linha = lexema.linha#Guarda a linha que ocorre atribuição
                    valor = ""#guarda a expressão da atribuição
                    for lexemaAT in tabelaDeTokens[comeco+2:]:#percorre cada token da atribuição
                        if(linha !=lexemaAT.linha):#se acabou a linha pare
                            break
                        if(lexemaAT.token.tipo == "id"):#se for id deve pegar o valor do "id"
                            try:
                                aux = self.tabelaDeSimbolos.getIdentificador(lexemaAT.lexema)
                                valor=valor+aux
                            except:
                                raise ErroSemantico(u"Erro semântico:'%s' não foi declarada "%lexemaAT.lexema)
                        else:
                            valor=valor+lexemaAT.lexema
                        indiceTabelaSimbolos+=1#Quando voltar pro laço inicial não verificará mais a linha da atribuição
                    #Add o identificador a tabela de símbolos
                    identificador = Identificador(lexema,eval(valor),type(eval(valor)),escopoAtual)                       
                    self.tabelaDeSimbolos.addIdentificador(identificador)
                              
            indiceTabelaSimbolos+=1
            
            
            
            
        
        
        
        