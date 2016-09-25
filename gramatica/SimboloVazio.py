'''
Created on 19 de set de 2016

@author: Raul
'''
from gramatica.Terminal import *


class SimboloVazio(Terminal):
    '''
    classdocs
    '''

    def __init__(self,simbolo="e"):
        super().__init__(simbolo)
        