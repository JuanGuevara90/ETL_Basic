import random
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QLabel 
from PyQt5.QtChart import QChart, QChartView, QValueAxis, QBarCategoryAxis, QBarSet, QBarSeries, QLineSeries
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPainter
from PyQt5 import QtCore, QtGui, QtWidgets


from connectorBDD import * # Se importa los metodos de acceso y consulta a la BDD


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
        self.tabs.addTab(self.tab3, "Horas de uso")  
        self.tabs.addTab(self.tab4, "Horas de uso por laboratorio")  
        self.tabs.addTab(self.tab5, "Estudiantes")  
        self.tabs.addTab(self.tab6, "Horas de uso por mes")  
        # Create first tab 
        
        # Gráficos de reservaciones por ciclo---------------------------------------------------------------------------
        self.tab1.layout = QVBoxLayout(self) 
        self.conn = connector() # Generar el conector
        df_1 = reservacionesPorCiclo(self.conn)   # Se realiza la consulta y se devuelve en formato DataFrame
        val_max_g1 = df_1['contador'].max() # Se determina el valor maximo de columna para generar el rango maximo del eje Y
        lista_periodos_g1=[]  # Estrucuta que almacenara las etiquetas y valores para cada periodo
        series = QBarSeries()  # Estructura donde se almacena los valores de cada serie

        for index, row in df_1.iterrows():  # Bucle para almanceanar los datos en la estructura dada por PyChart
            lista_periodos_g1.append(QBarSet(row['Periodo']))
            lista_periodos_g1[index].append(row['contador'])
            series.append(lista_periodos_g1[index])

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

        #Reservaciones por laboratorio-------------------------------------------------------------------------

        self.tab2.layout = QVBoxLayout(self)
        list_QBarSet_g2=[] # Estructura de datos para graficar

        df_contarPeriodos = contarPeriodos(self.conn)
        df_contarLaboratorios = contarLaboratorios(self.conn)
        df_g2= reservacionesPorLaboratorio(self.conn)
        val_max_g2 = df_g2['contador'].max() # Se determina el valor maximo de columna para generar el rango maximo del eje Y

        for index, row in df_contarPeriodos.iterrows():
            list_QBarSet_g2.append(QBarSet(row['Periodo']))

        series_bar = QBarSeries()
        lis_laboratorio=() # Estructura para almacenar los nombres de los laboratorio
        lis_laboratorio = list(lis_laboratorio)
        for index,row in df_contarLaboratorios.iterrows():
            lis_laboratorio.insert(index, row["Image"])
            for index_2,row_2 in df_contarPeriodos.iterrows():
                find_value=df_g2.loc[(df_g2['Periodo'] == str(row_2["Periodo"]))&(df_g2['Image'] == str(row["Image"]))] 
                if find_value.empty:
                    list_QBarSet_g2[index_2].append(0)
                else:
                    value_get=find_value['contador'].iloc[0]
                    list_QBarSet_g2[index_2].append(value_get)
            
        
        for index_3, row in df_contarPeriodos.iterrows():     
            series_bar.append(list_QBarSet_g2[index_3])

        chart = QChart()
        chart.addSeries(series_bar)
        chart.setTitle('Reservaciones por laboratorio')
        chart.setAnimationOptions(QChart.SeriesAnimations)

        axisX = QBarCategoryAxis()
        axisX.append(lis_laboratorio)
        axisY = QValueAxis()
        axisY.setRange(0, val_max_g2)
        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignLeft)
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
        self.chartView_2 = QChartView(chart)
        self.tab2.layout.addWidget(self.chartView_2 ) 
        self.tab2.setLayout(self.tab2.layout) 


        # Gráficos de horas de uso---------------------------------------------------------------------------
        self.tab3.layout = QVBoxLayout(self) 
        df_3 = horasDeUso(self.conn)   # Se realiza la consulta y se devuelve en formato DataFrame
        val_max_g3 = df_3['contador'].max() # Se determina el valor maximo de columna para generar el rango maximo del eje Y
        lista_periodos_g3=[]  # Estrucuta que almacenara las etiquetas y valores para cada periodo
        series_3 = QBarSeries()  # Estructura donde se almacena los valores de cada serie

        for index, row in df_3.iterrows():  # Bucle para almanceanar los datos en la estructura dada por PyChart
            lista_periodos_g3.append(QBarSet(row['Periodo']))
            lista_periodos_g3[index].append(row['contador'])
            series_3.append(lista_periodos_g3[index])

        chart = QChart()
        chart.addSeries(series_3)
        chart.setTitle('Horas de uso')
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

        self.chartView_3 = QChartView(chart)
        self.tab3.layout.addWidget(self.chartView_3 ) 
        self.tab3.setLayout(self.tab3.layout) 


        #Horas de Uso por laboratorio-------------------------------------------------------------------------

        self.tab4.layout = QVBoxLayout(self)
        list_QBarSet_g4=[] # Estructura de datos para graficar

        df_g4= horasDeUsoPorLaboratorio(self.conn)
        val_max_g4 = df_g4['contador'].max() # Se determina el valor maximo de columna para generar el rango maximo del eje Y
        #val_min_g4 = df_g4['contador'].min() # Se determina el valor maximo de columna para generar el rango maximo del eje Y

        for index, row in df_contarPeriodos.iterrows():
            list_QBarSet_g4.append(QBarSet(row['Periodo']))

        series_bar_4 = QBarSeries()

        lis_laboratorio=()
        lis_laboratorio = list(lis_laboratorio)
        for index,row in df_contarLaboratorios.iterrows():
            lis_laboratorio.insert(index, row["Image"])
            for index_2,row_2 in df_contarPeriodos.iterrows():
                find_value=df_g4.loc[(df_g4['Periodo'] == str(row_2["Periodo"]))&(df_g4['Image'] == str(row["Image"]))] 
                if find_value.empty:
                    list_QBarSet_g4[index_2].append(0)
                else:
                    value_get=find_value['contador'].iloc[0]
                    list_QBarSet_g4[index_2].append(value_get)
            
        
        for index_3, row in df_contarPeriodos.iterrows():     
            series_bar_4.append(list_QBarSet_g4[index_3])

        chart = QChart()
        chart.addSeries(series_bar_4)
        chart.setTitle('Horas de Uso por laboratorio')
        chart.setAnimationOptions(QChart.SeriesAnimations)

        months = lis_laboratorio

        axisX = QBarCategoryAxis()
        axisX.append(months)
        axisY = QValueAxis()
        axisY.setRange(0, val_max_g4)
        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignLeft)
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
        self.chartView_4 = QChartView(chart)
        self.tab4.layout.addWidget(self.chartView_4 ) 
        self.tab4.setLayout(self.tab4.layout) 

        # Gráficos de Estudiantes---------------------------------------------------------------------------
        self.tab5.layout = QVBoxLayout(self) 
        df_5 = estudiantes(self.conn)   # Se realiza la consulta y se devuelve en formato DataFrame
        val_max_g5= df_5['contador'].max() # Se determina el valor maximo de columna para generar el rango maximo del eje Y
        lista_periodos_g5=[]  # Estrucuta que almacenara las etiquetas y valores para cada periodo
        series_5 = QBarSeries()  # Estructura donde se almacena los valores de cada serie

        for index, row in df_5.iterrows():  # Bucle para almanceanar los datos en la estructura dada por PyChart
            lista_periodos_g5.append(QBarSet(row['Periodo']))
            lista_periodos_g5[index].append(row['contador'])
            series_5.append(lista_periodos_g5[index])

        chart = QChart()
        chart.addSeries(series_5)
        chart.setTitle('Estudiantes')
        chart.setAnimationOptions(QChart.SeriesAnimations)

        text = ('Período')

        axisX = QBarCategoryAxis()
        axisX.append(text)
        axisY = QValueAxis()
        axisY.setRange(0, val_max_g5)
        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignLeft)
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        self.chartView_5 = QChartView(chart)
        self.tab5.layout.addWidget(self.chartView_5 ) 
        self.tab5.setLayout(self.tab5.layout) 

        #Horas de uso por mes----------------------------------------------------------------------------------------
        self.tab6.layout = QVBoxLayout(self) 

        df_6 = horasUsoPorMes(self.conn)
        val_max_g6 = df_6['contador'].max() # Se determina el valor maximo de columna para generar el rango maximo del eje Y
        series_6 = QLineSeries() # Estructura donde se almacena los valores de cada serie
        lis_mes_ano=() # Estructura para almacenar mes y el año
        lis_mes_ano = list(lis_mes_ano)

        for index, row in df_6.iterrows():  # Bucle para almanceanar los datos en la estructura dada por PyChart
            lis_mes_ano.insert(index,str(int(row['Ano'])) +"/"+ str(int(row['Mes'])))
            series_6.append((index+1), row['contador'])

        chart = QChart()
        chart.addSeries(series_6)
        chart.setTitle('Horas de Uso por Mes')
        chart.setAnimationOptions(QChart.SeriesAnimations)

        axisX = QBarCategoryAxis()
        axisX.append(lis_mes_ano) # monthos
        axisY = QValueAxis()
        axisY.setRange(0, val_max_g6)
        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignLeft)
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
        self.chartView_6 = QChartView(chart)
        self.tab6.layout.addWidget(self.chartView_6 ) 
        self.tab6.setLayout(self.tab6.layout) 


        self.layout.addWidget(self.tabs) 
        self.setLayout(self.layout) 
if __name__ == '__main__': 
    app = QApplication(sys.argv) 
    ex = App() 
    sys.exit(app.exec_())