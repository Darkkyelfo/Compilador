# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(607, 665)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 601, 601))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.t_console = QtGui.QTextEdit(self.tab)
        self.t_console.setEnabled(False)
        self.t_console.setGeometry(QtCore.QRect(0, 400, 591, 171))
        self.t_console.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.t_console.setObjectName(_fromUtf8("t_console"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 591, 391))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.t_linhaNumeros = QtGui.QTextEdit(self.horizontalLayoutWidget)
        self.t_linhaNumeros.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t_linhaNumeros.sizePolicy().hasHeightForWidth())
        self.t_linhaNumeros.setSizePolicy(sizePolicy)
        self.t_linhaNumeros.setMaximumSize(QtCore.QSize(50, 16777215))
        self.t_linhaNumeros.setStyleSheet(_fromUtf8("background-color: rgb(198, 198, 198);\n"
"color: rgb(0, 0, 0);"))
        self.t_linhaNumeros.setObjectName(_fromUtf8("t_linhaNumeros"))
        self.horizontalLayout.addWidget(self.t_linhaNumeros)
        self.t_digitar = QtGui.QTextEdit(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t_digitar.sizePolicy().hasHeightForWidth())
        self.t_digitar.setSizePolicy(sizePolicy)
        self.t_digitar.setMaximumSize(QtCore.QSize(550, 16777215))
        self.t_digitar.setSizeIncrement(QtCore.QSize(0, 0))
        self.t_digitar.setStyleSheet(_fromUtf8(""))
        self.t_digitar.setObjectName(_fromUtf8("t_digitar"))
        self.horizontalLayout.addWidget(self.t_digitar)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.t_traducao = QtGui.QTextEdit(self.tab_2)
        self.t_traducao.setEnabled(False)
        self.t_traducao.setGeometry(QtCore.QRect(0, 0, 561, 551))
        self.t_traducao.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.t_traducao.setObjectName(_fromUtf8("t_traducao"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.b_compilar = QtGui.QPushButton(self.centralwidget)
        self.b_compilar.setGeometry(QtCore.QRect(440, 610, 99, 27))
        self.b_compilar.setObjectName(_fromUtf8("b_compilar"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Compilador", None))
        self.t_linhaNumeros.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Editor", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tradução", None))
        self.b_compilar.setText(_translate("MainWindow", "Compilar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

