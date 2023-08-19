import random
import time

MOVIMIENTOS = ["piedra", "papel", "tijera"]
MENSAJES = {
    "intro": "--- ¡Piedra, Papel o Tijera! ---\n",
    "elige": "¿Qué eliges?",
    "espera": "\nLa PC está eligiendo...",
    "resultados": "\n--- Resultados ---"
}

class Juego:
    def __init__(self):
        self.punctuacion = {'jugador': 0, 'pc': 0}

    def eleccion_pc(self):
        time.sleep(1.5)
        print(random.choice(["\nNo sé que elegir...", "\nDéjame pensar...", "\nEsta es difícil..."]))
        time.sleep(1)
        return random.choice(MOVIMIENTOS)

    def jugar():