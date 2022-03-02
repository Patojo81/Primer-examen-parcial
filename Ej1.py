import os
from numpy import empty 
import psycopg2
import time
import random
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
    print ("\t1 - Jugar 8")
    print ("\t2 - Ver historial")
    print ("\t0 - SALIR")


while True:
    os.system('cls')
    menu()
    print ("")
    opcionMenu = input("        Seleccione una opcion >>")

    if opcionMenu=="1": 
         try:
            sj= True
            while sj:
            
             print ("Jugando 8")
             print ("")
             pdado = random.randint(1,6)
             sdado = random.randint(1,6)
             print(pdado)
             print(sdado)
             suma = pdado + sdado
             print("La suma es igual a", suma)
             cursor = conexion.cursor()
             cursor.execute("INSERT INTO ej1(dado1, dado2, suma) VALUES(%s,%s,%s);", (pdado,sdado,suma))
             conexion.commit()
             cursor.close()

             if suma == 7 :
                sj = False
                input("Ud Perdio...\nPresiona cualquier tecla para volver al menu")
             else:
                sj = True
             if suma == 8 :
                sj = False
                input("Ud Gano...\nPresiona cualquier tecla para volver al menu")
             else:
                sj = True
        
         except:
            print ("Ocurrio un error")
            print("")
            input("Presiona cualquier tecla para volver al menu")

    if opcionMenu=="2":
     try:
         
        os.system('cls')
        cursor = conexion.cursor()
        SQL = 'SELECT*FROM ej1;'
        cursor.execute(SQL)
        valores= cursor.fetchall()
        print("Los valores ud los observara de la siguiente manera, (dado 1, dado 2, Suma)")
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
