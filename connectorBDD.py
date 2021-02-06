import mysql.connector
import pandas as pd
from pandas.io import sql
from sqlalchemy import create_engine
###
import datetime as dt # Libreria para el manejo de fechas

def connector():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="info_utpl",
            port='3306'
        )
        return conn
    except Exception as e:
        print("Error de conexión")



#Inserciones en la BDD
def insertTable(conn,df):
    try:
        df_total=df
        sql= """INSERT INTO data_reg (User_Group,User,Image,Hours,Reservations,Date_start_reservation,Date_end_reservations,Ano,Mes,Dia,Periodo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        mycursor = conn.cursor()
        for index, row in df_total.iterrows():
            Date_start_reservation=pd.to_datetime(row['Date_start_reservation'],yearfirst = True) # Se establece el formato de datetime
            Date_end_reservations=pd.to_datetime(row['Date_end_reservations'],yearfirst = True) # Se establece el formato de datetime
            mycursor.execute(sql, (row['User Group'],row['User'],row['Image'],row['Hours'],row['Reservations'],Date_start_reservation,Date_end_reservations,row['Año'],row['Mes'],row['Dia'],row['Periodo']))
            
        conn.commit()

    except Exception as e:
        conn.close()
        print(e)


#------------------------------------------------------------ Consultas a la BDD ------------------------------------------------------------------------------
# Contar el numero de periodo
def contarPeriodos(conn):
    try:
        my_data = pd.read_sql("SELECT DISTINCT Periodo FROM data_reg",conn)
        #print(my_data)
        return my_data
    except Exception as e:
        conn.close()
        print(e)
        return "Error"

def contarLaboratorios(conn):
    try:
        my_data = pd.read_sql("SELECT DISTINCT Image FROM data_reg",conn)
        #print(my_data)
        return my_data
    except Exception as e:
        conn.close()
        print(e)
        return "Error"



#Reservaciones por ciclo bien

def reservacionesPorCiclo(conn):
    try:
        my_data = pd.read_sql("SELECT Periodo, count(*) as contador FROM data_reg group by Periodo order by Ano asc",conn)
        #print(my_data)
        return my_data
    except Exception as e:
        conn.close()
        print(e)
        return "Error"

#Reservaciones por Laboratorio: 
def reservacionesPorLaboratorio(conn):
    try:
        my_data = pd.read_sql("SELECT Image, Periodo,count(*)  as contador FROM data_reg group by Periodo,Image order by Image, Ano asc",conn)
        #print(my_data)
        return my_data
    except Exception as e:
        conn.close()
        print(e)
        return "Error"


#Horas de uso :   
def horasDeUso(conn):
    try:
        #my_data = pd.read_sql("SELECT Date_start_reservation, Date_end_reservations,TIMESTAMPDIFF(HOUR, Date_start_reservation, Date_end_reservations )   FROM data_reg ",conn)
        my_data = pd.read_sql("SELECT Periodo,sum(TIMESTAMPDIFF(HOUR, Date_start_reservation, Date_end_reservations )) AS contador   FROM data_reg group by Periodo order by Ano asc",conn)
        #print(my_data)
        return my_data
    except Exception as e:
        conn.close()
        print(e)
        return "Error"


#Horas de uso por laboratorio
def horasDeUsoPorLaboratorio(conn):
    try:
        my_data = pd.read_sql("SELECT Image,Periodo, SUM(TIMESTAMPDIFF(HOUR, Date_start_reservation, Date_end_reservations )) as contador  FROM data_reg group by Periodo,Image order by Image asc",conn)
        #my_data = pd.read_sql("SELECT Periodo,sum(TIMESTAMPDIFF(HOUR, Date_start_reservation, Date_end_reservations ))   FROM data_reg group by Periodo",conn)
        #print(my_data)
        return my_data
    except Exception as e:
        conn.close()
        print(e)
        return "Error"


#Estudiantes
def estudiantes(conn):
    try:
        my_data = pd.read_sql("SELECT Periodo, count(distinct User) as contador FROM data_reg group by Periodo order by Ano, Mes asc",conn)
        #print(my_data)
        return my_data
    except Exception as e:
        conn.close()
        print(e)
        return "Error"


#Horas de Uso por Mes
def horasUsoPorMes(conn):
    try:
        my_data = pd.read_sql("SELECT Ano,Mes, SUM(TIMESTAMPDIFF(HOUR, Date_start_reservation, Date_end_reservations )) as contador  FROM data_reg group by Ano,Mes order by Ano,Mes asc",conn)
        #my_data = pd.read_sql("SELECT Periodo,sum(TIMESTAMPDIFF(HOUR, Date_start_reservation, Date_end_reservations ))   FROM data_reg group by Periodo",conn)
        #print(my_data)
        return my_data
    except Exception as e:
        conn.close()
        print(e)
        return "Error"
    


conn =connector()
horasUsoPorMes(conn)
#reservacionesPorCiclo(conn)
#reservacionesPorLaboratorio(conn)
#contarPeriodos(conn)
#contarLaboratorios(conn)
#horasDeUsoPorLaboratorio(conn)
#horasDeUso(conn)
#estudiantes(conn)
#insertTable(conn)
