'''
Created on 7 de nov de 2016

@author: Raul
'''
# -*- coding:utf-8 -*-
from semantico.Escopo import Escopo
from semantico.ErroSemantico import ErroSemantico
from semantico.Identificador import Identificador
from semantico.FuncId import FuncId
from semantico.TabelaDeSimbolos import TabelaDeSimbolos

class AnalisadorSemantico(object):
    u'''
    Classe que é responsável por realizar a analise semântica
    '''
    def __init__(self):
        self.tDeFuncoes = TabelaDeSimbolos()
        self.tiposEscopos = ("if","else","while","def")#guarda os tipos de escopo
        self.dentroLaco = ("break","continue")#palavras chaves que só devem existir dentro do "while"
        self.escopo = Escopo()
    
    def analiseSemantica(self,tabelaDeTokens):
        escopoAtual = self.escopo
        indiceTabelaSimbolos = 0
        tamanho = len(tabelaDeTokens)
        while(indiceTabelaSimbolos<tamanho):
            lexema=tabelaDeTokens[indiceTabelaSimbolos]
            if(lexema.token.tipo in self.tiposEscopos):#localiza os escopos
                if(lexema.token.tipo=="def"):#Declarações de funções possuem sua própria tabela de simbolos
                    filho = Escopo(escopoAtual,len(escopoAtual.escoposFilhos),lexema.token.tipo,TabelaDeSimbolos())
                else:
                    filho = Escopo(escopoAtual,len(escopoAtual.escoposFilhos),lexema.token.tipo,escopoAtual.tabelaDeSimbolos)
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
                                identificador = Identificador(lexemaAux,0,"parametro",escopoAtual)  
                                escopoAtual.tabelaDeSimbolos.addIdentificador(identificador)  
                                parametros+=1
                            elif(lexemaAux.token.tipo=="numero"):
                                raise ErroSemantico(u"Erro semântico: declaração de funções ou procedimentos deve possuir somente variáveis")
                            elif(lexemaAux.token.tipo==")"):
                                break    
                        funcId = FuncId(lexema,0,None,escopoAtual,parametros)
                        self.tDeFuncoes.addIdentificador(funcId)
                       # self.tabelaDeSimbolos.addIdentificador(funcId)
                    else:#Caso não seja uma declaração de função e sim uma chamada
                        try:
                            funcao = self.tDeFuncoes.getIdentificador(lexema.lexema)#Verifica se a função já foi declarada
                        except:
                            raise ErroSemantico(u"Erro semântico:a função '%s' não foi declarada "%lexema.lexema)
                        
                        numPara = 0
                        for parametro in tabelaDeTokens[comeco+1:]:#checa se o número de argumentos da função está correto
                            if(parametro.token.tipo=="id" or parametro.token.tipo=="numero"):
                                numPara+=1
                            elif(parametro.token.tipo==")"):
                                break 
                        if(numPara != funcao.argumentos):
                            raise ErroSemantico(u"Erro semântico:%s Número de argumentos errado"%funcao.lexema.lexema)  
                            
            #Esse "if" é responsavel por tratar todos os acontecimentos associados a uma variável  
            elif(lexema.token.tipo == "id"):
                comeco = indiceTabelaSimbolos
                if(tabelaDeTokens[comeco+1].token.tipo=="="):#quando ocorre uma atribuição
                    linha = lexema.linha#Guarda a linha que ocorre atribuição
                    valor = ""#Guarda a expressão da atribuição
                    for lexemaAT in tabelaDeTokens[comeco+2:]:#percorre cada token da atribuição
                        if(linha !=lexemaAT.linha):#se acabou a linha pare
                            break
                        if(lexemaAT.token.tipo == "id"):#se for id deve pegar o valor do "id"
                            try:
                                aux = escopoAtual.tabelaDeSimbolos.getIdentificador(lexemaAT.lexema)
                            except:
                                raise ErroSemantico(u"Erro semântico:'%s' não foi declarada "%lexemaAT.lexema)
                            valor = self.__validarExpressao(valor,str(aux.valor))
                        else:
                            valor = valor + lexemaAT.lexema
                        indiceTabelaSimbolos+=1#Quando voltar pro laço inicial não verificará mais a linha da atribuição
                    #Add o identificador a tabela de símbolos
                    identificador = Identificador(lexema,eval(valor),type(eval(valor)),escopoAtual)  
                    escopoAtual.tabelaDeSimbolos.addIdentificador(identificador)                  
                    #self.tabelaDeSimbolos.addIdentificador(identificador)
                else:#Caso a variavel apareça em outro lugar(ifs,whiles ou returns) 
                    try:
                        escopoAtual.tabelaDeSimbolos.getIdentificador(lexema.lexema)
                    except:#Se ela não for declarada antes da Erro
                        raise ErroSemantico(u"Erro semântico:'%s' não foi declarada "%lexema.lexema)
            indiceTabelaSimbolos+=1
            
    #determina se a expressão é válida
    #por exemplo: Se a = True e s = a + 3 
    #isso deve dar erro
    def __validarExpressao(self,expressao,novoElemento):
        tipo =  type(eval(novoElemento))
        if(tipo==bool):
            raise ErroSemantico(u"Erro semântico:A expressão'%s' é inválida"%(expressao+novoElemento))
        expressaoValida = expressao + novoElemento
        return expressaoValida
       
           
           
            
            
        
        
        
        