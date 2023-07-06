import numpy
import os
entrada_platinum = 120000
entrada_gold = 80000
entrada_silver = 50000
lista_ruts = []
lista_filas = []
lista_columnas = []

def ver_menu_compra():
    print(f""" Menú entradas
    1. Entrada Platinum {entrada_platinum}
    2. Entrada Gold     {entrada_gold}
    3. Entrada Silver   {entrada_silver}         
     """)

def ver_menu():
    print("""
    1. Comprar entradas
    2. Mostrar ubicaciones disponibles
    3. Ver listado de asistentes
    4. Mostrar ganancias totales
    5. Salir
    """)
    
def validar_opcion():
    while True:
        try:
            opcion = int(input("ingrese su opcion"))
            if opcion in(1,2,3,4,5):
                return opcion         
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO")
    
concierto = numpy.zeros((10,10), int)    
    
def ver_escenario(): 
    print("           ESCENARIO")
    for x in range(10):
        print(f"fila {x+1}  ", end=" ")
        for y in range(10):
            print(concierto [x][y], end=" ")
        print()
    print("columna  1 2 3 4 5 6 7 8 9 10")
              
def validar_rut():
    while True:  
        try:
            rut = int(input("ingrese su rut(sin punto ni digito verificador)"))
            if len(str(rut)) >= 7 and len(str(rut)) <= 8:
                return rut              
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO")   
        
def validar_fila():
    while True:
        try:
            fila = int(input("ingrese su fila"))
            if fila >= 1 and fila <=10:
                return fila       
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO")
        
def validar_columna():
    while True:
        try:
            columna = int(input("ingrese la columna")) 
            if columna >= 1 and columna <= 10:
                return columna         
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO")

def cantidad_entradas():
    asistente = input("ingrese la cantidad de entradas")
    for x in range(1,3):
        return asistente

contador = 0
acumulador = 0

def comprar_entradas():
    if 0 not in concierto:
        print("No quedan asientos disponibles")
    else:
        cantidad_entradas()
        ver_escenario()
        ver_menu_compra()
        rut = validar_rut()
        fila = validar_fila()
        columna = validar_columna()
        if concierto[fila-1][columna-1]==0:
            concierto[fila-1][columna-1]=1
        lista_ruts.append(rut)
        lista_filas.append(fila)
        lista_columnas.append(columna)
        print("La operación se ha realizado correctamente")
                
def ver_asistentes():
    (lista_ruts>lista_ruts)
    print("los asistentes son", lista_ruts)
    
def salir():
    print("Felipe Vega", "06-07-2023")

