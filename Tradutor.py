'''
Created on 19 de fev de 2017

@author: raulu
'''
from lexico.TabelaDeTokens import TabelaDeTokens

class Tradutor3Enderecos(object):
    '''
    classdocs
    '''
    
    def __init__(self,tabelaDeTokens):
        self.tabela = tabelaDeTokens
        self.traducao = ""
        
    def converter(self):
        for i,lex in enumerate(self.tabela):
            if(lex.token.tipo == "="):
                atribuicao,tamanho = self.__coletarAtb(i-1,lex.linha)
                atribuicao = self.__converterAtribuicao(atribuicao,tamanho)
                print(atribuicao)
        pass
    
    
    def __converterAtribuicao(self,atribuicao,qtVar):
        sinais = ["*","/","+","-"]
        quadrupla = []
        atribuicao = atribuicao.replace("=",":=")
        qtAtual = qtVar
        varTemp = 0
        while True:
            if(qtAtual-2<=3):
                temp=""
                ant = ""
                for atr in quadrupla:
                    temp=temp+ atr[3]+":="+atr[1]+atr[0]+atr[2]+"\n"
                    temp= temp.replace("§",ant)
                    ant = atr[3]
                atribuicao = temp +"\n"+ atribuicao.replace("§","t"+str(varTemp))
                return atribuicao
            else:
                for sinal in sinais:
                    if(sinal in atribuicao):
                        p = atribuicao.index(sinal)
                        varTemp+=1
                        quadrupla.append([atribuicao[p],atribuicao[p-1],atribuicao[p+1],"t"+str(varTemp)])
                        atribuicao = atribuicao.replace(atribuicao[p-1:p+2],"§")
                        qtAtual = qtAtual - 2 
                        break
             
            
    
    
    def __conveterIf(self):
        pass
        

    def __converterWhile(self):
        pass
    
    def __coletarAtb(self,indice,linha):
        atribuicao = ""
        variaveis = 0
        for variavel in self.tabela[indice:]:
            if(variavel.linha!=linha):
                break
            atribuicao+=variavel.lexema
            variaveis+=1
        return atribuicao,variaveis 
            
        
        