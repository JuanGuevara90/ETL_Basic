# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from graphics import Ui_MainWindow_Graphics # Importación de la pantalla de gráficos
import re  # Libreria para el manejo de Expresiones regulares
from PyQt5.QtWidgets import QMessageBox # Libreria para mostrar un cuadro de dialogo

from connectorBDD import createTable # Libreria crear la BDD y la tabla
from connectorBDD import connector


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #Parametros de configuracion de la ventana y tambien los elementos que la constituyen
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(436, 300)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(0, 0, 200, 100));")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonIngresar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonIngresar.setGeometry(QtCore.QRect(40, 200, 100, 50))
        self.pushButtonIngresar.setObjectName("pushButtonIngresar")

        self.pushButtonSalir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSalir.setGeometry(QtCore.QRect(290, 200, 100, 50))
        self.pushButtonSalir.setObjectName("pushButtonSalir")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(60, 70, 311, 111))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 30, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 60, 16))
        self.label_2.setObjectName("label_2")
        self.lineEditPassword = QtWidgets.QLineEdit(self.frame)
        self.lineEditPassword.setGeometry(QtCore.QRect(90, 60, 191, 21))
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.lineEditPassword.setStyleSheet("QLineEdit{background:white}")
        self.lineEditUsuario = QtWidgets.QLineEdit(self.frame)
        self.lineEditUsuario.setGeometry(QtCore.QRect(90, 30, 191, 21))
        self.lineEditUsuario.setObjectName("lineEditUsuario")
        self.lineEditUsuario.setStyleSheet("QLineEdit{background:white}")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 20, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButtonLimpiar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonLimpiar.setGeometry(QtCore.QRect(160, 200, 100, 50))
        self.pushButtonLimpiar.setObjectName("pushButtonLimpiar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.msg = QMessageBox() # Inicializacion de cuadro de dialogo

        self.pushButtonIngresar.clicked.connect(self.mybutton_clicked_Ingresar) # Evento de pulsar el boton ingresar
        self.pushButtonLimpiar.clicked.connect(self.mybutton_clicked_Limpiar) # Evento de pulsar el boton limpiar
        self.pushButtonSalir.clicked.connect(self.mybutton_clicked_Salir) # Evento de pulsar el boton salir
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def mybutton_clicked_Ingresar(self): # Funcion para capturar el click del boton ingresar
        self.ventana= QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_Graphics()
        self.ui.setupUi(self.ventana)

        # Validación de Email usando expresiones regulares
        self.usuario = self.lineEditUsuario.text()
        emailRegex = r'(\W|^)[\w.\-]{0,25}@(utpl)\.edu\.ec(\W|$)' # Expresión regular para el mail que contenga @utpl.edu.ec
        match = re.search(emailRegex, self.usuario) # Match de la cadena de ingreso con la expresión regular valor a devolver verdadero o falso
        if match:
            self.msg.setWindowTitle("Ingreso Correcto")
            self.msg.setText("Bienvenido al aplicativo !!!")
            self.x = self.msg.exec_()
            self.conn = connector()  # Generando conexión a la BDD
            createTable(self.conn)
            MainWindow.close() # Cerrar la pantalla de login
            self.ventana.show() # Abrir la ventana de gráficos
        else:
            self.msg.setWindowTitle("Alerta...!!!")
            self.msg.setText("Por favor verfique los datos ingresados")
            self.x = self.msg.exec_()
        
    def mybutton_clicked_Limpiar(self): # Funcion para capturar el click del boton ingresar
        self.retranslateUi(MainWindow)
        MainWindow.close()
        MainWindow.show()

    def mybutton_clicked_Salir(self): # Funcion para capturar el click del boton salir
        sys.exit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.pushButtonIngresar.setText(_translate("MainWindow", "Ingresar"))
        self.pushButtonSalir.setText(_translate("MainWindow", "Salir"))
        self.label.setText(_translate("MainWindow", "Usuario"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.label_3.setText(_translate("MainWindow", "INFO UTPL"))
        self.pushButtonLimpiar.setText(_translate("MainWindow", "Limpiar"))
        self.lineEditUsuario.setText('')
        self.lineEditPassword.setText('')
        
        self.pushButtonIngresar.setStyleSheet(_translate("MainWindow","QPushButton{background-color : qlineargradient(spread:pad,x1:0, y1:0, x2:1, y2:0, stop:0 white, stop: 1 rgb(185,37,37)); border-style: solid;border-radius:21px;font-weight: bold;}QPushButton::pressed{background-color : red;}"))
        self.pushButtonSalir.setStyleSheet(_translate("MainWindow","QPushButton{background-color : qlineargradient(spread:pad,x1:0, y1:0, x2:1, y2:0, stop:0 white, stop: 1 rgb(67,180,72));border-style: solid;border-radius:21px;font-weight: bold;}QPushButton::pressed{background-color : rgb(0,255,0);}"))
        self.pushButtonLimpiar.setStyleSheet(_translate("MainWindow","QPushButton{background-color : qlineargradient(spread:pad,x1:0, y1:0, x2:1, y2:0, stop:0 white, stop: 1 #F2BE22);border-style: solid;border-radius:21px;font-weight: bold;}QPushButton::pressed{background-color : yellow;}"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())