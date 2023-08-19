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
        self.puntuacion = {'jugador': 0, 'pc': 0}

    def eleccion_pc(self):
        time.sleep(1)
        print(random.choice(["\nNo sé que elegir...", "\nDéjame pensar...", "\nEsta es difícil..."]))
        time.sleep(1)
        return random.choice(MOVIMIENTOS)

    def jugar(self, eleccion_jugador):
        eleccion_pc = self.eleccion_pc()
        combinaciones_ganadoras = [("piedra", "tijera"), ("papel", "piedra"), ("tijera", "papel")]

        print(MENSAJES["resultados"])
        print(f"Jugador: {eleccion_jugador} vs. PC: {eleccion_pc}\n")

        if eleccion_jugador == eleccion_pc:
            return "¡Es un empate!"
        elif (eleccion_jugador, eleccion_pc) in combinaciones_ganadoras:
            self.puntuacion['jugador'] += 1
            return "¡Ganaste!"
        else:
            self.puntuacion['pc'] += 1  # Se añade el punto al PC aquí
            return "Perdiste :("

    def mostrar_puntuacion(self):
        return f"Puntuación 🏆 -> Jugador: {self.puntuacion['jugador']} | 🖥️ PC: {self.puntuacion['pc']}"

    def iniciar(self):
        print(MENSAJES["intro"])
        while True:
            for idx, movimiento in enumerate(MOVIMIENTOS, 1):
                print(f"{idx}. {movimiento.capitalize()}")
            print("4. Salir")

            eleccion = input("\n" + MENSAJES["elige"] + " (1-4): ")

            if eleccion == "4":
                print("\n¡Gracias por jugar!")
                print(self.mostrar_puntuacion())
                break

            if eleccion not in ["1", "2", "3"]:
                print("\nOpción no válida, intenta de nuevo...")
                continue

            eleccion_jugador = MOVIMIENTOS[int(eleccion) -1]
            print(MENSAJES["espera"])
            resultado = self.jugar(eleccion_jugador)
            print(resultado)
            print("\n" + self.mostrar_puntuacion())
            time.sleep(2)
            print("\n" + "-"*40 + "\n")

if __name__ == "__main__":
    juego = Juego()
    juego.iniciar()
