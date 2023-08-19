def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b if b != 0 else "No se puede dividir entre cero."

def main():
    ops = {
        "1": suma,
        "2": resta,
        "3": multiplicacion,
        "4": division
    }

    print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir")
    seleccion = input(": ")

    if seleccion not in ops:
        print("Opción no válida, intenta de nuevo...")
        return

    num1, num2 = float(input("Número 1: ")), float(input("Número 2: "))
    print("Resultado: ", ops[seleccion](num1, num2))

if __name__ == "__main__":
    main()