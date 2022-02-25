import os
from numpy import empty 
import psycopg2
import time
import random

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
    print ("\t1 - identificar numero")
    print ("\t2 - Ver historial")
    print ("\t0 - SALIR")


while True:

    menu()
    print ("")
    opcionMenu = input("        Seleccione una opcion >>")

    if opcionMenu=="1": 
         try:
             os.system('cls')
             print ("indicador de numeros primos")
             print ("")
             n=int(input("Ingrese un número: "))
             cursor = conexion.cursor()
             if n <= 0:
                 print("El número debe ser mayor que cero")
             else:
                cant_divisores = 0
                i = 1
                while (i <= n):
                    if n % i == 0:
                        cant_divisores+=1
                    i+=1
                if cant_divisores==2:
                    print("El número es primo")
                    res = "Número primo"
                    cursor.execute("insert into ej4(num) values(%s);",(n))
                    conexion.commit()
                else:
                    print("El número es compuesto")
                    res = "Número compuesto"
                    cursor.execute("insert into ej4(num) values(%s);",(n))
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
        SQL = 'SELECT*FROM ej4;'
        cursor.execute(SQL)
        valores= cursor.fetchall()
        print("Los valores ud los observara de la siguiente manera, (ultimo numero)")
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