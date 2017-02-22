'''
Created on 21 de fev de 2017

@author: raulu
'''
from GUI.telaPrincipal import Ui_MainWindow
from PyQt4 import QtGui
from Compilador import Compilador
from sintatico.ErroSintatico import ErroSintatico
from semantico.ErroSemantico import ErroSemantico
from lexico.TokenInvalidoError import TokenInvalidoError
class JanelaPrincipal(QtGui.QMainWindow,Ui_MainWindow):

        def __init__(self,parent=None):
            super().__init__(parent)
            self.setupUi(self)
            self.compilador = Compilador()
            self.b_compilar.clicked.connect(self.__compilar)
            self.t_digitar.textChanged.connect(self.__contarLinhas)
            self.t_linhaNumeros.verticalScrollBar().valueChanged.connect(
            self.t_digitar.verticalScrollBar().setValue)
            
            self.t_digitar.verticalScrollBar().valueChanged.connect(
            self.t_linhaNumeros.verticalScrollBar().setValue)
        def __compilar(self):
            try:
                self.t_console.setPlainText("")
                self.compilador.compilar(self.t_digitar.toPlainText())
                self.t_traducao.setPlainText(self.compilador.traducao)
                self.t_console.setPlainText("O código Está correto")
            except (TokenInvalidoError) as e:
                self.t_console.setPlainText(str(e))
            except(ErroSintatico) as e:
                self.t_console.setPlainText(str(e))
            except(ErroSemantico) as e:
                self.t_console.setPlainText(str(e))
        
        def __contarLinhas(self):
            if(len(self.t_digitar.toPlainText())>0):
                l = self.t_digitar.toPlainText().count("\n")
                linhas = 1
                numLinhas = str(linhas)
                for i in range(l):
                    numLinhas +="\n"+str(i+linhas+1) 
                self.t_linhaNumeros.setPlainText(numLinhas)
            else:
                self.t_linhaNumeros.setPlainText("")

           
            
            
        