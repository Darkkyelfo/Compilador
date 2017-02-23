'''
Created on 25 de set de 2016

@author: Raul
'''
#encoding:utf-8
from gramatica.Gramatica import Gramatica
from sintatico.Pilha import Pilha
from sintatico.TabelaSintatica import TabelaSintatica
from lexico.TabelaDeTokens import TabelaDeTokens
from gramatica.Variavel import Variavel
from gramatica.Terminal import Terminal
from gramatica.SimboloVazio import SimboloVazio
from sintatico.ErroSintatico import ErroSintatico
class AnalisadorSintatico(object):
    u'''
        Classe responsavel por representar o analisador sintático
        ela recebe a gramática e a tabela Sintática para poder funcionar
        -IDEIA: posteriormente ela deve receber somente a gramática e a apartir dela construir
        a tabela
    '''


    def __init__(self,gramatica):
        self.__gramatica = self.__seperarGramatica(gramatica)
        self.tabelaSintatica = None#Atributo que armazena a tabela sintática. Será trocado por private futuramente.
        self.gramaIni  = gramatica.getPrimeiraVar()
        self.__pilha = None
    
    #Método responsavel por deixar a gramatica em um formata mais simples para
    #se indexar com a tabela
    def __seperarGramatica(self,gramaticaNaoSepada):
        gramaticaSeparada = []
        for var in gramaticaNaoSepada.getListaProducoes():
            for prod in var.producao:
                prod.reverse()#inverte a produção para facilitar o processo de empilhar
                gramaticaSeparada.append(prod)
        return gramaticaSeparada 
    
    def analisarSintaxe(self,tabelaDeTokens,linhaIni=0):
        self.__pilha= Pilha(self.gramaIni)
        for lexema in tabelaDeTokens:
            self.__analisarLexema(lexema,linhaIni)
        for i in range(self.__pilha.getTamanho()):#Caso restem produções na pilha tem que verificar se elas vão para o vazio
            if(isinstance(self.__pilha.topo(),Variavel) and self.__pilha.topo().temVazio):
                self.__pilha.pop()#Se forem desempilhe 
        if(self.__pilha.getTamanho()!=0):#Caso a pilha não esteja vazia           
            raise ErroSintatico("Erro sintático no caracter:%s linha:%s"%(lexema.lexema,lexema.linha))  
        return True
    
    #Determina que regra deve ser chamada 
    # e empilha e desempilha a pilha      
    def __analisarLexema(self,lexema,linhaIni):
        achouTerminal = False
        while(achouTerminal==False):
            if(self.__pilha.getTamanho()>0 and isinstance(self.__pilha.topo(),Variavel)):#se for uma variavel vai procurar na tabela o que ela gera
                regra=self.tabelaSintatica.consultarTabela(self.__pilha.topo(),lexema)
                if(regra==None):#erro 
                    raise ErroSintatico("Erro sintático no caracter:%s linha:%s"%(lexema.lexema,lexema.linha))#Localiza a regra a ser aplicada
                else:#Se a regra é válida            
                    self.__pilha.pop()
                    for elemento in self.__gramatica[regra-linhaIni]:
                        if(isinstance(elemento,SimboloVazio)==False):
                            self.__pilha.push(elemento)   
            else:#Se não for variável é um terminal 
                if(self.__pilha.topo().simbolo==lexema.token.tipo): 
                    self.__pilha.pop()
                    achouTerminal = True 
                else:#erro
                    raise ErroSintatico("Erro sintático no caracter:%s linha:%s"%(lexema.lexema,lexema.linha))
                    
    def imprimirGramatica(self):
        cont= 0
        for i in self.__gramatica:
            cont+=1
            print("%s."%cont , end="")
            for j in i:
                print(j.simbolo, end=" ")
            print("\n")    
        