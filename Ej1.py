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
    print ("\t1 - Jugar 8")
    print ("\t0 - SALIR")

while True:
    menu()
    print ("")
    opcionMenu = input("        Seleccione una opcion >>")

    if opcionMenu=="1": 
         try:
            sj= True
            while sj:
             os.system('cls')
             print ("Usted a elegido Jugar 8")
             print ("")
             pdado = random.randint(1,6)
             sdado = random.randint(1,6)
             print(pdado)
             print(sdado)
             suma = pdado + sdado
             print(suma)

             if suma == "7" :
                sj = False
                
             else:
                sj = True
        
         except:
            print ("Alguno de los caracteres introducidos no es un numero")
            print("")
            input("Presiona cualquier tecla para volver al menu")