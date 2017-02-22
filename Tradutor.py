'''
Created on 19 de fev de 2017

@author: raul
'''
from semantico.Escopo import Escopo
class Tradutor3Enderecos(object):
    
    def __init__(self,tabelaDeTokens):
        self.tabela = tabelaDeTokens
        self.tiposEscopos = ("if","else","while","def")#guarda os tipos de escopo
        self.traducao = ""
        self.escopoAtual = None
        self.label = 0#Salva a numeracao dos labels
        
    def converter(self):
        self.traducao = ""#guarda o resultado da tradução
        self.escopoAtual = Escopo()#guarda o escopo atual
        for i,lex in enumerate(self.tabela):
            sentenca = ""#Guarda o trecho que está sendo traduzido
            if(lex.token.tipo in self.tiposEscopos):
                self.label+=1
                #Atualiza o escopo atual
                escopoFilho = Escopo(self.escopoAtual,0,lex.token.tipo)
                escopoFilho.label=self.label
                self.escopoAtual.addFilho(escopoFilho)
                self.escopoAtual = escopoFilho
                
                if(lex.token.tipo=="else"):#Coloca label do "else" 
                    sentenca = "L"+str(self.escopoAtual.label-1)+":"+"\n"
                elif(lex.token.tipo == "def"):
                    sentenca = "func begin "+self.tabela[i+1].lexema.replace("(","")+"\n"
                    self.escopoAtual.nomeFunc = self.tabela[i+1].lexema
                else:
                    sentenca = self.__traducaoSentenca(i+2)    
            elif(lex.token.tipo == "="):
                sentenca,tamanho = self.__coletarAtb(i-1,lex.linha)
                sentenca = self.__converterAtribuicao(sentenca,tamanho)
            elif(lex.token.tipo=="funcId" and self.escopoAtual.tipo!="def"):#Traduz as chamadas de função
                sentenca = self.__tFuncCall(i)
            elif(lex.lexema=="}"):
                if(self.escopoAtual.tipo=="while"):
                    sentenca = "goto " + "L"+str(self.escopoAtual.label)+":"+"\n" + "L"+str(self.escopoAtual.label+1)+":"+"\n"
                elif(self.escopoAtual.tipo=="if" and self.tabela[i+1].token.tipo=="else"):
                    sentenca = "goto " + "L"+str(self.escopoAtual.label+2)+"\n"
                elif(self.escopoAtual.tipo=="else"):#Coloca o label para onde ir depois de excutar o "if". Impedindo de executar o "else" se o "if" for ativado 
                    sentenca = "L"+str(self.escopoAtual.label)+":"+"\n"
                elif(self.escopoAtual.tipo == "def"):
                    sentenca = "func end "+self.tabela[i+1].lexema.replace("(","")+"\n"
                else:
                    sentenca = "L"+str(self.escopoAtual.label+1)+":"+"\n"
                self.escopoAtual = self.escopoAtual.escopoPai
                
            self.traducao += sentenca
        return self.traducao
    
    #traduz as chamadas de função
    def __tFuncCall(self,indice):
        sentenca = ""
        parametros = 0
        nomeFunc = self.tabela[indice].lexema
        for sen in self.tabela[indice+2:]:#começar a pecorrer após o "("
            if(sen.lexema==")"):
                break
            if(sen.lexema!=","):
                sentenca+="param "+sen.lexema+"\n"
                parametros+=1
        sentenca = sentenca+"call "+nomeFunc.replace("(","")+","+str(parametros)+"\n"
        return sentenca
            
    #Traduz as senteças de "if","while"
    def __traducaoSentenca(self,indice):
        sentenca = ""
        for sen in self.tabela[indice:]: 
            if(sen.lexema==")"):
                break
            sentenca +=sen.lexema
            
        traducao = "L"+str(self.escopoAtual.label)+": if " + sentenca + " goto L"+str(self.escopoAtual.label+1)+"\n"
        self.label+=1
        return traducao
    
    #Lê a tabela e monta a expressão de atribuição
    def __coletarAtb(self,indice,linha):
        atribuicao = ""
        variaveis = 0
        for variavel in self.tabela[indice:]:
            if(variavel.linha!=linha):
                break
            atribuicao+=variavel.lexema
            variaveis+=1
        return atribuicao,variaveis 
    
    #Converta a atribução para 3 endereços
    #Usa uma tabela quadrupla
    def __converterAtribuicao(self,atribuicao,qtVar):
        sinais = ["*","/","+","-"]
        quadrupla = []
        atribuicao = atribuicao.replace("=",":=")
        qtAtual = qtVar#Quantidade de elementos atualmente na expressão
        varTemp = 0
        while True:
            if(qtAtual-2<=3):#Deve ter 3 ou menos. Ignorando "a="
                temp=""
                ant = ""
                qLinha = ""
                for atr in quadrupla:#Lẽ a quadrupla e monta a string de tradução
                    temp=temp+qLinha+atr[3]+":="+atr[1]+atr[0]+atr[2] 
                    temp= temp.replace("§",ant)
                    ant = atr[3]
                    qLinha = "\n"
                atribuicao = temp +qLinha+ atribuicao.replace("§","t"+str(varTemp))
                return atribuicao
            else:#monta as quadruplas
                for sinal in sinais:
                    if(sinal in atribuicao):
                        p = atribuicao.index(sinal)
                        varTemp+=1
                        quadrupla.append([atribuicao[p],atribuicao[p-1],atribuicao[p+1],"t"+str(varTemp)])
                        atribuicao = atribuicao.replace(atribuicao[p-1:p+2],"§")
                        qtAtual = qtAtual - 2 
                        break   
                
                  
        
        
        
        
    
            
        
        