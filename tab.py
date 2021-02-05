import random
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QLabel 
from PyQt5.QtChart import QChart, QChartView, QValueAxis, QBarCategoryAxis, QBarSet, QBarSeries
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPainter
from PyQt5 import QtCore, QtGui, QtWidgets


from connectorBDD import connector # Importación del conector a la BDD
from connectorBDD import reservacionesPorCiclo # Importación para ejecutar la consulta de la BDD y devolver el valor en DataFrame

import sys 
# Creating the main window 
class App(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        self.title = 'Info UTPL'
        self.left = 200
        self.top = 200
        self.right = 200
        self.bottom = 200
        self.width = 1800
        self.height = 700
        self.setWindowTitle(self.title) 
        self.setGeometry(self.left, self.top, self.width, self.height) 
        self.tab_widget = MyTabWidget(self) 
        self.setCentralWidget(self.tab_widget) 
        self.show() 
# Creating tab widgets 
class MyTabWidget(QWidget): 
    def __init__(self, parent): 
        super(QWidget, self).__init__(parent) 
        self.layout = QVBoxLayout(self) 
        # Initialize tab screen 
        self.tabs = QTabWidget() 
        self.tab1 = QWidget() 
        self.tab2 = QWidget() 
        self.tab3 = QWidget() 
        self.tab4 = QWidget() 
        self.tab5 = QWidget() 
        self.tab6 = QWidget() 
        self.tabs.resize(300, 200) 
        self.pushButton_2=QPushButton()
        self.pushButton_2.resize(0, 200) 

        # Add tabs 
        self.tabs.addTab(self.tab1, "Reservaciones por ciclo") 
        self.tabs.addTab(self.tab2, "Reservaciones por Laboratorio") 
        self.tabs.addTab(self.tab3, "Horas de uso por laboratorio")  
        self.tabs.addTab(self.tab4, "Horas de uso por laboratorio")  
        self.tabs.addTab(self.tab5, "Estudiantes")  
        self.tabs.addTab(self.tab6, "Horas de uso por mes")  
        # Create first tab 
        self.tab1.layout = QVBoxLayout(self) 

        # Gráficos de reservaciones por ciclo

        #Periodos

        self.conn = connector() # Generar el conector
        df_1 = reservacionesPorCiclo(self.conn)   # Se realiza la consulta y se devuelve en formato DataFrame
        val_max_g1 = df_1['contador'].max() # Se determina el valor maximo de columna para generar el rango maximo del eje Y
        lista_peridos_g1=[]  # Estrucuta que almacenara las etiquetas y valores para cada periodo
        series = QBarSeries()  # Estructura donde se almacena los valores de cada serie

        for index, row in df_1.iterrows():  # Bucle para almanceanar los datos en la estructura dada por PyChart
            lista_peridos_g1.append(QBarSet(row['Periodo']))
            lista_peridos_g1[index].append(row['contador'])
            series.append(lista_peridos_g1[index])

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle('Reservaciones por ciclo')
        chart.setAnimationOptions(QChart.SeriesAnimations)

        text = ('Períodos')

        axisX = QBarCategoryAxis()
        axisX.append(text)
        axisY = QValueAxis()
        axisY.setRange(0, val_max_g1)
        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignLeft)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        self.chartView = QChartView(chart)

        self.tab1.layout.addWidget(self.chartView ) 
        self.tab1.setLayout(self.tab1.layout) 


        #Reservaciones por laboratorio


        self.tab2.layout = QVBoxLayout(self) 

        set0 = QBarSet('X0')
        set1 = QBarSet('X1')
        set2 = QBarSet('X2')
        set3 = QBarSet('X3')
        set4 = QBarSet('X4')

        set0.append([random.randint(0, 10) for i in range(6)])
        set1.append([random.randint(0, 10) for i in range(6)])
        set2.append([random.randint(0, 10) for i in range(6)])
        set3.append([random.randint(0, 10) for i in range(6)])
        set4.append([random.randint(0, 10) for i in range(6)])

        series = QBarSeries()
        series.append(set0)
        series.append(set1)
        series.append(set2)
        series.append(set3)
        series.append(set4)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle('Bar Chart Demo')
        chart.setAnimationOptions(QChart.SeriesAnimations)

        months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun')

        axisX = QBarCategoryAxis()
        axisX.append(months)

        axisY = QValueAxis()
        axisY.setRange(0, 15)

        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignLeft)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        self.chartView_2 = QChartView(chart)

        self.tab2.layout.addWidget(self.chartView_2 ) 
        self.tab2.setLayout(self.tab2.layout) 



        # Add tabs to widget 
        self.layout.addWidget(self.tabs) 
        self.setLayout(self.layout) 
if __name__ == '__main__': 
    app = QApplication(sys.argv) 
    ex = App() 
    sys.exit(app.exec_())