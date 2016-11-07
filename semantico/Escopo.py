'''
Created on 7 de nov de 2016

@author: Raul
'''
#-*- coding:utf-8 -*-
class Escopo(object):
    u'''
    classe que representa um escopo. Vai auxiliar na para determinar onde o identificador
    foi chamado.
    '''


    def __init__(self,escopoPai = None,id = 0,tipo = "main"):
        self.escopoPai = escopoPai
        self.id = id
        self.tipo = tipo
        self.escoposFilhos = []
    
    
    def addFilho(self,escopoFilho):
        self.escoposFilhos.append(escopoFilho)
        
    

        
        