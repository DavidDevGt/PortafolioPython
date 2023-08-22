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