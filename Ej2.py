import os
from numpy import empty 
import psycopg2
import time
import random
import statistics
'#commit'
from pyparsing import Char 
try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password ="C3leste2112",
        dbname = "ejercicios"
    )
    os.system('cls')
    print("CONEXION CON LA BASE DE DATOS EXITOSA...")
    time.sleep(1) 
    os.system('cls')
    print("BIENVENIDO...")
    time.sleep(1) 

    os.system('cls')
except psycopg2.Error as e:
    print ("ocurrio un error en la conexion")
    print ("Verifique los parametros")
    time.sleep(2) 
    os.system('cls')

def menu():
    os.system('cls')
    print ("                  MENU")
    print ("\t1 - Operar calificaciones")
    print ("\t2 - Ver historial")
    print ("\t0 - SALIR")


while True:

    menu()
    print ("")
    opcionMenu = input("        Seleccione una opcion >>")

    if opcionMenu=="1": 
         try:
             os.system('cls')
             print ("Operando calificaciones")
             print ("")
             C1 = float(input ("Primera nota: "))
             C2 = float(input ("segunda nota: "))
             C3 = float(input ("Tercera nota: "))
             C4 = float(input ("Cuarta nota: "))
             C5 = float(input ("quinta nota: "))
             maximo=C1
             minimo=C1
             vn =[C1,C2,C3,C4,C5]
             if C2 >maximo:
                    maximo=C2
             if C3 >maximo:
                    maximo=C3
             if C4 >maximo:
                    maximo=C4
             if C5 >maximo:
                    maximo=C5

             if C2 <minimo:
                    minimo=C2
             if C3 <minimo:
                    minimo=C3
             if C4 <minimo:
                    minimo=C4
             if C5 <minimo:
                    minimo = C5
             rango = [maximo,minimo]
             media=((C1+C2+C3+C4+C5)/5)
             mediana= statistics.median(vn)
             moda =statistics.mode(vn)
             desviacion = statistics.stdev(vn)
             varianza = statistics.variance(vn)

             print("la media es >>   ",media)
             print("la mediana es >>",statistics.median(vn))
             print("la moda es >>",statistics.mode(vn))
             print("el rango es >>   ",rango)
             print("la desviacion estandar es >>",statistics.stdev(vn))
             print("la Varianza estandar es >>",statistics.variance(vn))
            
             input("Presiona cualquier tecla para volver al menu")
             cursor = conexion.cursor()
             cursor.execute("INSERT INTO ej3(calificacion1,calificacion2,calificacion3,calificacion4,calificacion5,media,moda,mediana,maximo,minimo,desviacion,varianza) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);", (C1,C2,C3,C4,C5,media,mediana,moda,maximo,minimo,desviacion,varianza))
             conexion.commit()
             cursor.close()
         except:
            print ("Ocurrio un error")
            print("")
            input("Presiona cualquier tecla para volver al menu")

    if opcionMenu=="2":
     try:
         
        os.system('cls')
        cursor = conexion.cursor()
        SQL = 'SELECT*FROM ej3;'
        cursor.execute(SQL)
        valores= cursor.fetchall()
        print("Los valores ud los observara de la siguiente manera, (calificacion1,calificacion2,calificacion3,calificacion4,calificacion5,media,moda,mediana,maximo,minimo,desviacion,varianza)")
        print("")
        print(valores)
        print("")
        input("Estos son los valores encontrados...\nPresiona cualquier tecla para volver al menu")
        conexion.commit()
        cursor.close()
     except:
            os.system('CLS')
            input("no se pudieron obtener los valores\nPresiona cualquier tecla para volver al menu")
            os.system('CLS')

    if opcionMenu=="0":             
        os.system('cls')
        print ("Saliste")
        conexion.close()
        break