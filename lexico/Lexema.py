'''
Created on 30 de ago de 2016

@author: Raul
'''
#-*- coding:utf-8 -*-
class Lexema(object):
    
    def __init__(self,nome,token,linha,posicao):
        self.lexema=nome
        self.token = token
        self.linha=linha
        self.posicao=posicao
    
    #Sobrecarga do operador de igualdade("==")
    def __eq__(self, outro):
        if(self.lexema==outro.lexema and  self.token==outro.token and self.linha == outro.linha
           and self.posicao==outro.posicao):
            return True
        return False
        
    
        