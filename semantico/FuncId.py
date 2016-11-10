'''
Created on 10 de nov de 2016

@author: Raul
'''
from semantico.Identificador import Identificador
#-*- coding:utf-8 -*-
class FuncId(Identificador):
    '''
        Representa o identificador de funções para ser colocado na tabaleDeSimbolos
    '''

    def __init__(self,lexema,valor,tipo,escopo,argumentos):
        super().__init__(lexema,valor,tipo,escopo)
        self.argumentos = argumentos
        