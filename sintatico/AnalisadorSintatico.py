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
        self.__pilha = Pilha(gramatica.getPrimeiraVar())
    
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
        try:
            for lexema in tabelaDeTokens:
                self.__analisarLexema(lexema,linhaIni)
        except(ErroSintatico) as e:
            print(str(e))
            return False
        if(self.__pilha.getTamanho()!=0):             
            return False
        return True
           
    def __analisarLexema(self,lexema,linhaIni):
            achouTerminal = False
            while(achouTerminal==False):
                if(self.__pilha.getTamanho()>0 and isinstance(self.__pilha.top(),Variavel)):#se for uma variavel vai procurar na tabela o que ela gera
                    regra=self.tabelaSintatica.consultarTabela(self.__pilha.top(),lexema) 
                    if(regra==None):#erro 
                        raise ErroSintatico("Erro sintático no caracter:%s linha:%s"%(lexema.lexema,lexema.linha))
                    else:#Se a regra é válida 
                        self.__pilha.pop()
                        for elemento in self.__gramatica[regra-linhaIni]:
                            if(isinstance(elemento,SimboloVazio)==False):
                                self.__pilha.push(elemento)
                else:#Se não for variável é um terminal 
                    if(self.__pilha.top().simbolo==lexema.token.tipo): 
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
        