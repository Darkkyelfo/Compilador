'''
Created on 30 de ago de 2016
@author: Raul
'''
#-*-encoding:uft-8-*-
import sys
from CompiladorGUI import JanelaPrincipal
from PyQt4 import QtGui

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    av = JanelaPrincipal()
    av.show()
    sys.exit(app.exec_())

