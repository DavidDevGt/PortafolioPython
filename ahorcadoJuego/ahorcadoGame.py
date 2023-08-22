import random
import os

class Ahorcado:
    def __init__(self):
        self.palabras_tecnologia = {
            'Lenguajes de Programación': ['python', 'golang', 'javascript', 'ruby', 'visual basic'],
            'Frameworks': ['django', 'react', 'flask', 'angular', 'svelte', 'react native', 'vue']
        }
        self.categoria = ''
        self.palabra = ''
        self.intentos = 5
        self.letras_adivinadas = []
        self.letras_intentadas = []
        self.fin_juego = False

    def seleccionar_palabra(self):
        self.categoria = random.choice(list(self.palabras_tecnologia.keys()))
        self.palabra = random.choice(self.palabras_tecnologia[self.categoria])

    def mostrar_tablero(self):
        return ''.join([letra if letra in self.letras_adivinadas else '_' for letra in self.palabra])

    def intentar_letra_o_palabra(self, entrada):
        if len(entrada) > 1:  # Se intenta una palabra
            if entrada == self.palabra:
                self.letras_adivinadas = list(self.palabra)
                return 'acertada_palabra'
            else:
                self.intentos -= 2
                return 'fallo_palabra'

        if entrada in self.letras_intentadas:  # Se intenta una letra que ya se probó antes
            return 'repetida'
        self.letras_intentadas.append(entrada)
        if entrada in self.palabra:  # La letra está en la palabra
            self.letras_adivinadas.append(entrada)
            return 'acertada'
        else:  # La letra no está en la palabra
            self.intentos -= 1
            return 'fallo'

    def juego_completado(self):
        if "_" not in self.mostrar_tablero():
            return True
        if self.intentos <= 0:
            return True
        return False

    def interfaz_juego(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + "-" * 50)
        print("*Iniciando el Juego del Ahorcado*")
        print("-" * 50)
        print(f"Categoría: {self.categoria}")
        print(f"Palabra a adivinar: {self.mostrar_tablero()}")
        print(f"Intentos restantes: {self.intentos}")
        print(f"Letras intentadas: {' '.join(self.letras_intentadas)}")
        if self.fin_juego:
            if self.intentos <= 0:
                print(f"\nHas perdido. La palabra era: {self.palabra}")
            else:
                print(f"\n¡Felicitaciones! Adivinaste la palabra: {self.palabra}")

    def jugar(self):
        self.seleccionar_palabra()
        while not self.juego_completado():
            self.interfaz_juego()
            entrada = input("\nIntroduce una letra o la palabra completa: ").lower()
            resultado = self.intentar_letra_o_palabra(entrada)
            if resultado == 'repetida':
                input("\nYa intentaste esa letra. Pulsa enter para continuar.")
            elif resultado == 'fallo':
                input("\nIncorrecto. Pulsa enter para continuar.")
            elif resultado == 'fallo_palabra':
                input("\nEsa no es la palabra. Has perdido 2 intentos. Pulsa enter para continuar.")
            else:
                input("\n¡Correcto! Pulsa enter para continuar.")
            self.fin_juego = self.juego_completado()
        self.interfaz_juego()

if __name__ == "__main__":
    juego = Ahorcado()
    juego.jugar()
