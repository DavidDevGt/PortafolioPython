def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b if b != 0 else "No se puede dividir entre cero."

def mostrar_menu():
    """Despliega el menú de opciones al usuario."""
    print("\nCalculadora:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    return input(": ")

def main():
    ops = {
        "1": suma,
        "2": resta,
        "3": multiplicacion,
        "4": division
    }

    while True:  # Bucle para mostrar el menú hasta que el usuario decida salir
        seleccion = mostrar_menu()

        if seleccion == '5':
            break
        elif seleccion not in ops:
            print("Opción no válida, intenta de nuevo...")
            continue

        num1 = float(input("Número 1: "))
        num2 = float(input("Número 2: "))
        print("Resultado: ", ops[seleccion](num1, num2))

if __name__ == "__main__":
    main()
