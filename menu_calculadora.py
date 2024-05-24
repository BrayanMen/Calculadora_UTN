import os
from operaciones_matematicas import *
    
def limpiar_terminal():
    os.system("cls")

def calculadora():
    num_a = None
    num_b = None
    opcion = None
    
    print("Bienvenido a la calculadora")
    while True:
        menu(num_a,num_b)
    
        ingresar_opcion = int(input("Elige un opcion: "))
        limpiar_terminal()    
            
        match(ingresar_opcion):
            case 1:
                if num_a == None:
                    num_a = int(input("Ingresar el primer operando: "))
                else:
                    num_a = int(input("Nuevo primer operando: "))
            case 2:
                if num_b == None:
                    num_b = int(input("Ingresar el segundo operando: "))
                else:
                    num_b = int(input("Nuevo segundo operando: "))
            case 3:
                if num_a == None or num_b == None:
                    print("Debes ingresas los Operandos.")
                    input("Presiona Enter para continuar...")
                    limpiar_terminal()
                else:
                    while True:
                        menu_operaciones()
                        opcion = str(input("Elige una opcion: "))
                        limpiar_terminal()                          
                        if opcion in ['a','b','c','d','e','f']:
                            break
                        else:
                            if opcion == 'g':
                                opcion = None
                                break
                            else:
                                print("Opción no válida, intenta de nuevo.")
                                input("Presiona Enter para continuar...")
                                limpiar_terminal()            
            case 4:
                if opcion is None:
                    print("Primero seleccione una operación a realizar.")
                    input("Presiona Enter para continuar...")
                    limpiar_terminal()
                else:
                    prints_operaciones(opcion,num_a,num_b)
                    input("Presiona Enter para continuar...")
                    limpiar_terminal()    
            case 5:
                limpiar_terminal()
                print("Muchas gracias, hasta luego.")
                break
    
calculadora()