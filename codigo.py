def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero."

# Función principal
def calculadora():
    print("Calculadora Simple")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = input("Seleccione la operación (1/2/3/4): ")

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == '1':
        resultado = sumar(num1, num2)
    elif opcion == '2':
        resultado = restar(num1, num2)
    elif opcion == '3':
        resultado = multiplicar(num1, num2)
    elif opcion == '4':
        resultado = dividir(num1, num2)
    else:
        print("Opción no válida.")
        return

    print("Resultado:", resultado)
    print("linea de prueb")


# Llamar a la calculadora
calculadora()
