'''
Created on 30 de ago de 2016

@author: Raul
'''
#-*-encoding:utf-8-*-

class Token(object):
    def __init__(self,tipo,expRegular,ignorar=False):
        self.tipo = tipo
        self.expRegular = expRegular
        self.ignorar = ignorar

        