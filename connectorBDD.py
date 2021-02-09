import sqlite3
import pandas as pd


def createTable(conn):
    try:
        mycursor= conn.cursor()
        mycursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='data_reg' ''')
        if mycursor.fetchone()[0]!=1 :
            mycursor.execute("CREATE TABLE data_reg(id INTEGER PRIMARY KEY AUTOINCREMENT,User_Group text no null,User text no null ,Image text not null,Hours integer not null,Reservations integer not null,Date_start_reservation datetime not null,Date_end_reservations not null,Ano integer not null, Mes not null, Dia not null, Periodo not null)")
    except Exception as e:
        print("Error")

def connector():
    try:
        conn = sqlite3.connect('info_utpl.db')
        return conn
    except Exception as e:
        print("Error de conexión")


#Inserciones en la BDD
def insertTable(conn,df):
    try:
        df_total=df
        sql= """INSERT INTO data_reg (User_Group,User,Image,Hours,Reservations,Date_start_reservation,Date_end_reservations,Ano,Mes,Dia,Periodo) VALUES (?,?,?,?,?,?,?,?,?,?,?)"""
        mycursor = conn.cursor()

        for index, row in df_total.iterrows():
            formatted_date_star=pd.to_datetime(row['Date_start_reservation'],yearfirst = True) # Se establece el formato de datetime
            Date_start_reservation = formatted_date_star.strftime('%Y-%m-%d %H:%M:%S')
            formatted_date_end=pd.to_datetime(row['Date_end_reservations'],yearfirst = True) # Se establece el formato de datetime
            Date_end_reservations= formatted_date_end.strftime('%Y-%m-%d %H:%M:%S')
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
        my_data = pd.read_sql("Select Periodo, sum(Cast ((JulianDay(Date_end_reservations) - JulianDay(Date_start_reservation)) * 24 As Integer)) as contador from data_reg group by Periodo order by Ano asc",conn)
        #print(my_data)
        return my_data
    except Exception as e:
        conn.close()
        print(e)
        return "Error"


#Horas de uso por laboratorio
def horasDeUsoPorLaboratorio(conn):
    try:
        my_data = pd.read_sql("SELECT Image,Periodo,  sum(Cast ((JulianDay(Date_end_reservations) - JulianDay(Date_start_reservation)) * 24 As Integer)) as contador  FROM data_reg group by Periodo,Image order by Image asc",conn)
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
        my_data = pd.read_sql("SELECT Ano,Mes, sum(Cast ((JulianDay(Date_end_reservations) - JulianDay(Date_start_reservation)) * 24 As Integer)) as contador  FROM data_reg group by Ano,Mes order by Ano,Mes asc",conn)
        #my_data = pd.read_sql("SELECT Periodo,sum(TIMESTAMPDIFF(HOUR, Date_start_reservation, Date_end_reservations ))   FROM data_reg group by Periodo",conn)
        #print(my_data)
        return my_data
    except Exception as e:
        conn.close()
        print(e)
        return "Error"

