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
        print(f"[1] Ingresar 1er operando(A = {"x" if num_a == None else num_a})")
        print(f"[2] Ingresar 2do operando(B = {"y" if num_b == None else num_b})")
        print("[3] Calcular operaciones")
        print("[4] Informar resultados")
        print("[5] Salir")
    
        ingresar_opcion = int(input("Elige un opcion: "))
        limpiar_terminal()    
            
        match(ingresar_opcion):
            case 1:
                num_a = int(input("Ingresar el primer operando: "))
            case 2:
                num_b = int(input("Ingresar el segundo operando: "))
            case 3:
                if num_a == None or num_b == None:
                    print("Debes ingresas los Operandos.")
                else:
                    while True:
                        print("Elige una opcion")
                        print("[a] Suma")
                        print("[b] Resta")
                        print("[c] Multiplicación")
                        print("[d] Division")
                        print("[e] Factorial")
                        print("[f] Secuencia Fibonacci")
                        print("[g] Volver al menú principal")
                        opcion = str(input("Elige una opcion: "))
                        limpiar_terminal()  
                        
                        if opcion == 'g':
                            opcion = None
                            break
                        else:
                            print("Opción no válida, intenta de nuevo.")                 
            case 4:
                if opcion is None:
                    print("Primero seleccione una operación a realizar.")
                    continue
                else:
                    match opcion:
                        case 'a':
                            print(f"El resultado de {num_a} + {num_b} es: {suma(num_a, num_b)}")
                        case 'b':
                            print(f"El resultado de {num_a} - {num_b} es: {resta(num_a, num_b)}")
                        case 'c':
                            print(f"El resultado de {num_a} * {num_b} es: {multiplicacion(num_a, num_b)}")
                        case 'd':
                            if num_b == 0:
                                print("Error: División por cero no permitida.")
                            else:
                                print(f"El resultado de {num_a} / {num_b} es: {division(num_a, num_b)}")
                        case 'e':
                            print(f"El factorial de {num_a} es: {factorial(num_a)}")
                            print(f"El factorial de {num_b} es: {factorial(num_b)}")
                        case 'f':
                            print(f"La secuencia de Fibonacci de {num_a} es: {fib(num_a)}")
                            print(f"La secuencia de Fibonacci de {num_b} es: {fib(num_b)}")
                        case 'g':
                            break
                        
                    continuar = input("¿Deseas continuar operando? (s/n): ").lower()
                    if continuar == 's':
                        limpiar_terminal()
                        break
                    else:
                        if continuar == 'n':
                            limpiar_terminal()
                            opcion = None
                            break
                        else:
                            print("Opción no válida, intenta de nuevo.")
            case 5:
                print("Muchas gracias, hasta luego.")
                break
    
calculadora()
    
    
