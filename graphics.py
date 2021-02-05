# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphics.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import sys,random
import os # Libreria para el manejo de archivos
from PyQt5.QtWidgets import QMessageBox # Libreria para mostrar un cuadro de dialogo
import pandas as pd # Libreria para el manejo de datos


from manual import Ui_MainWindow_Manual # Importacion de la clase manual
from files import JoinFile  # Importación del archivo donde se realiza la consolidacion de los datos
from tab import App   # Importacion del archivo tab donde se llama todas las gráficas
from connectorBDD import insertTable
from connectorBDD import connector


class Ui_MainWindow_Graphics(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(535, 223)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 531, 171))
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setGeometry(QtCore.QRect(30, 20, 211, 131))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButtonMigracion = QtWidgets.QPushButton(self.frame)
        self.pushButtonMigracion.setGeometry(QtCore.QRect(30, 20, 151, 41))
        self.pushButtonMigracion.setObjectName("pushButtonMigracion")
        self.pushButtonGraficar = QtWidgets.QPushButton(self.frame)
        self.pushButtonGraficar.setGeometry(QtCore.QRect(30, 70, 151, 41))
        self.pushButtonGraficar.setObjectName("pushButtonGraficar")
        self.frame_2 = QtWidgets.QFrame(self.groupBox)
        self.frame_2.setGeometry(QtCore.QRect(270, 20, 231, 131))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButtonManual = QtWidgets.QPushButton(self.frame_2)
        self.pushButtonManual.setGeometry(QtCore.QRect(40, 20, 151, 41))
        self.pushButtonManual.setObjectName("pushButtonManual")
        self.pushButtonSalir = QtWidgets.QPushButton(self.frame_2)
        self.pushButtonSalir.setGeometry(QtCore.QRect(40, 70, 151, 41))
        self.pushButtonSalir.setObjectName("pushButtonSalir")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 535, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.msg = QMessageBox() # Inicializacion del cuadro de dialogo
        self.pushButtonGraficar.setEnabled(False)

        self.retranslateUi(MainWindow)

        self.pushButtonMigracion.clicked.connect(self.mybutton_clicked_Migrar) # Evento de pulsar el boton graficar
        self.pushButtonGraficar.clicked.connect(self.mybutton_clicked_Graficar) # Evento de pulsar el boton graficar
        self.pushButtonManual.clicked.connect(self.mybutton_clicked_Manual_Usuario) # Evento de pulsar el boton manual de usuario
        self.pushButtonSalir.clicked.connect(self.mybutton_clicked_Salir) # Evento de pulsar el boton salir del programa
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def mybutton_clicked_Migrar(self): # Funcion para almacernar el contenido de los archivos xls y xlsx
        try:
            fname = QtWidgets.QFileDialog.getExistingDirectory()
            files = os.listdir(fname)  
            self.df_total=JoinFile(files)
            self.conn = connector()  # Generando conexión a la BDD
            insertTable(self.conn,self.df_total) # Inserción a la BDD
            self.msg.setText("Migración Correcta..!!")
            x = self.msg.exec_()
            self.pushButtonGraficar.setEnabled(True)  # Se activa el boton graficar una vez realizada la migración
            

        except Exception as e:
            self.pushButtonGraficar.setEnabled(False)
            self.msg.setText("Por favor seleccione el archivo correcto")
            x = self.msg.exec_()
            print(e)

    def mybutton_clicked_Graficar(self):
        self.ventana= QtWidgets.QMainWindow()
        self.ui = App()


    def mybutton_clicked_Manual_Usuario(self): # Funcion para capturar el click del boton manual de usuario
        self.ventana= QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_Manual()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        
    def mybutton_clicked_Salir(self): # Funcion para capturar el click del boton salir
        sys.exit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Info UTPL"))
        self.pushButtonMigracion.setText(_translate("MainWindow", "Migración de Datos"))
        self.pushButtonGraficar.setText(_translate("MainWindow", "Gráficar"))
        self.pushButtonManual.setText(_translate("MainWindow", "Manual de Usuario"))
        self.pushButtonSalir.setText(_translate("MainWindow", "Salir"))
