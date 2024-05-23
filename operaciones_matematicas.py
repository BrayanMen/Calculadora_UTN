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

