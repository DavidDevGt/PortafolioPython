import random
import os

class Ahorcado:
    def __init__(self):
        self.palabras_tecnologia = {
            'Lenguajes': ['python', 'javascript', 'ruby', 'visual basic'],
            'Frameworks': ['django', 'react', 'flask', 'angular', 'react native', 'vue']
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

    def intentar_letra(self, letra):
        if letra in self.letras_intentadas:
            return 'repetida'
        self.letras_intentadas.append(letra)
        if letra in self.palabra:
            self.letras_adivinadas.append(letra)
            return 'acertada'
        else:
            self.intentos -= 1
            return 'fallo'

    def juego_completado(self):
        if "_" not in self.mostrar_tablero():
            return True
        if self.intentos == 0:
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
            if self.intentos == 0:
                print(f"\nHas perdido. La palabra era: {self.palabra}")
            else:
                print(f"\n¡Felicitaciones! Adivinaste la palabra: {self.palabra}")