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
    
    def consultarTabela(self,var,lexema):
        for linha,i in enumerate(self.linhas):
            if(i == var.simbolo):
                for coluna,j in enumerate(self.colunas):
                    if(j == lexema.token.tipo):
                        return self.matriz[linha][coluna]
                    
    def gerarTabelaArq(self,arquivo):
        arq = open(arquivo,"r")
        lista = arq.readlines()
        for i,linha in enumerate(lista):
            self.matriz.append([])
            for elemento in linha.split(";"):
                elemento = elemento.replace(" ","")
                elemento = elemento.replace('\n',"")
                if('|' in elemento):
                    elemento =elemento.replace('|',"")
                    self.colunas.append(elemento)
                elif(elemento.isupper()):
                    self.linhas.append(elemento)
                elif(elemento=="" and i!=0):
                    self.matriz[i].append(None)
                elif(elemento.isdigit()):
                    self.matriz[i].append(int(elemento))
        self.matriz.remove(self.matriz[0])
    
    def imprimir(self):
        for i in self.matriz:
            for j in i:
                print(j,end=" ")
            print("\n")
                    
            
                        
                    
        
                
                        
                
        