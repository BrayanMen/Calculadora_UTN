def suma(a:int, b:int)-> int:
    """Fucion para sumar 2 numeros

    Args:
        a (int): Primer Operando
        b (int): Segundo Operando

    Returns:
        int: Resultado de suma.
    """
    return a + b

def resta(a:int, b:int)->int:
    """Funcion para restar dos numeros

    Args:
        a (int): Primer Operando
        b (int): Segundo Operando

    Returns:
        int: Resultado de resta.
    """
    return a - b
    
def division(a: int, b: int)-> int:
    """Funcion que calcula division

    Args:
        a (int): Dividendo
        b (int): Divisor

    Returns:
        int: Resultado de la division si es posible, o mensaje de error si intenta dividir por 0
    """
    if b != 0:
        return a / b
    else:
       return print("No es posible dividir por cero")
        
def multiplicacion(a: int, b: int)-> int:   
    """Funcion que multiplica dos numeros

    Args:
        a (int): Primero numero
        b (int): Segundo numero

    Returns:
        int: Resultado de la multiplicacion
    """
    return a * b

def factorial(num: int)-> int:
    """Funcion que saca el factorial de un numero

    Args:
        num (int): Numero a calcular

    Returns:
        int: Factorial del numero
    """
    fact = 1
    if num == 0 and num == 1:
         fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact
            
def fib(num: int)-> int:
    """Secuencia Fibonacci

    Args:
        num (int): Ingresar un numero

    Returns:
        int: _description_
    """
    if num < 0:
        raise ValueError("El término de Fibonacci no puede ser negativo")
    else:
        if num == 0:
            return 0
        else:
            if num == 1:
                return 1
    a = 0
    b = 1
    for _ in range(2, num + 1):
        a = b 
        b = a + b
    return b

def menu(x:int, y:int):
    print("[1] Ingresar 1er operando (A = x)" if x == None else f"[1] Su 1er operando es: (A = {x})")
    print("[2] Ingresar 2do operando (B = y)" if y == None else f"[2] Su 2do operando es: (B = {y})")
    print("[3] Calcular operaciones")
    print("[4] Informar resultados")
    print("[5] Salir")
    
def menu_operaciones():
    print("Elige una opcion")
    print("[a] Suma")
    print("[b] Resta")
    print("[c] Multiplicación")
    print("[d] Division")
    print("[e] Factorial")
    print("[f] Secuencia Fibonacci")
    print("[g] Volver al menú principal")
    
def prints_operaciones(opcion, x:int, y:int):
    match opcion:
        case 'a':
            print(f"El resultado de {x} + {y} es: {suma(x, y)}")
        case 'b':
            print(f"El resultado de {x} - {y} es: {resta(x, y)}")
        case 'c':
            print(f"El resultado de {x} * {y} es: {multiplicacion(x, y)}")
        case 'd':
            if y == 0:
                print("Error: División por cero no permitida.")
            else:
                print(f"El resultado de {x} / {y} es: {division(x, y)}")
        case 'e':
            print(f"El factorial de {x} es: {factorial(x)}")
            print(f"El factorial de {y} es: {factorial(y)}")
        case 'f':
            print(f"La secuencia de Fibonacci de {x} es: {fib(x)}")
            print(f"La secuencia de Fibonacci de {y} es: {fib(y)}")    
        case _: 
            print("Opción no válida, intenta de nuevo.")