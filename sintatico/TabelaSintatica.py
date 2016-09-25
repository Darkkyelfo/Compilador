'''
Created on 25 de set de 2016

@author: Raul
'''
from gramatica.Terminal import Terminal
from gramatica.Variavel import Variavel

#enconding:utf-8
class TabelaSintatica(object):
#Classe responsavel por representar a tabela que será usada na analise sintática tabular
#Guarda os indices das produções que devem ser add a pilha
   
    def __init__(self):
        self.linhas =[]#Vai guardas o nome das variáveis
        self.colunas = []#Vai guardas os terminais
        self.matriz = []
    
    def gerarTabela(self,posicoes):
        qtLinhas = len(self.linhas)
        qtColunas  = len(self.colunas)
        for i in range(qtLinhas):
            self.matriz.append([])
            for j in range(qtColunas):
                self.matriz[i].append(None)
                for p in posicoes:
                    if(p[0]==i and p[1]==j):
                        self.matriz[i][j]=p[3]
                        break
    
    def consultarTabela(self,var,terminal):
        for linha,i in enumerate(self.linhas):
            if(i.simbolo == var.simbolo):
                for coluna,j in enumerate(self.colunas):
                    if(j.simbolo == terminal.terminal):
                        return (linha,coluna)
                        
                    
        
                
                        
                
        