import time 
import os 
import random 
import csv

menu = 1 
guardar_pedido = []
sector = ""
contador_5 = 0
contador_10 = 0
contador_20 = 0 

#Definiendo función para seleccionar el sector de reparto 
def sectores_reparto (): 
    try:
        seleccion_sector = int(input("Seleccione sector de reparto: \n1. San Bernardo \n2. Buin \n3. Paine. Presione (1/2/3) para seleccionar el sector: "))
        
        if seleccion_sector == 1: 
            sector = "San Bernardo"
                    
        elif seleccion_sector == 2: 
            sector = "Buin"
        
        elif seleccion_sector == 3: 
            sector = "Paine"
        
        else: 
            print ("Error de selección. Debe ingresar valor (1/2/3).")
    except ValueError: 
        print ("Error. Debe ingresar una opción válida.") 
        
    
#Definiendo función para crear registro de pedido
def registrar_pedido (pedido): 
    nro_pedido = [random.randint(1, 1000) for _ in range(10)]
    cliente = input ("Ingrese nombre de cliente: ")
    direccion = input ("Ingrese dirección")
    sector = (sectores_reparto)
    saco_5kg = int(input ("¿Cuántos sacos de 5kg desea?: "))
    saco_10kg = int(input ("¿Cuántos sacos de 10kg desea?: "))
    saco_20kg = int(input("¿Cuántos sacos de 20kg desea?: "))
    
    nuevo_pedido = {'nro_pedido': nro_pedido, 'cliente': cliente, 'direccion': direccion, 'sector': sectores_reparto, 'saco_5kg':saco_5kg, 'saco_10kg': saco_10kg, 'saco_20kg':saco_20kg }
    pedido.append(nuevo_pedido)
    guardar_pedido(pedido)

#Definiendo función para imprimir lista de pedidos     
def lista_pedidos (pedido): 
    if pedido: 
       print ("Lista de pedidos: ")
       for i, pedido in enumerate(pedido, start=1):
           print (f"{i}. Numero de pedido: {pedido['nro_pedido']}, Cliente: {pedido['cliente']}, Dirección: {pedido['direccion']} 
                  sector{pedido[sectores_reparto]}, Saco 5kg{pedido[saco_5g]}, Saco 10kg{pedido[saco_10kg]}, Saco 20kg{pedido[saco_20kg]}") 
    else: 
        print ("No hay pedidos registrados.")
        
#Definiendo función para escritura de archivo csv        
def guardar_pedido(pedido):
    
    ruta_archivo = "pedido.csv"
    with open(ruta_archivo, "w", newline="") as archivo_csv:
        datos = ["nro_pedido", "cliente", "direccion", "sector", "Saco 5kg", "Saco 10kg", "Saco 20kg" ]
    escritor_csv = csv.DictWriter(archivo_csv, fieldnames=datos)
    escritor_csv.writeheader()
    for pedido in pedido:
        escritor_csv.writerow(pedido) 
        
#Entrando al menu:
 
    seleccion = int(input("Menú de opciones: \n1. Registrar pedido. \n2. Listar todos los pedidos. \n3. Imprimir hoja de ruta. \n4. Salir del programa."))
    while menu == 1:        
                   
        if seleccion == 1: 
            print ("Abriendo registro de pedido: ")
            time.sleep (2)
            os.system ("cls")    
            registrar_pedido ()            
                
        if seleccion == 2:
            print ("Cargando lista de pedidos...")
            time.sleep (2)
            os.system ("cls")         
            print (lista_pedidos)
            
        if seleccion == 3: 
            
            print ("Creando archivo de hoja de ruta: ")
            time.sleep (2)
            os.system ("cls")
            guardar_pedido ()
        
        if seleccion == 4: 
            break

      
            
            
            
            
            
            
            
            
            
            
            
 


    


            
            
            
            
            
            
            
            
            
            
        
       


        
       
            
        
    