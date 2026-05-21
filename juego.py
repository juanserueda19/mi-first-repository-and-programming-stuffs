import random

def jugar():
    # La computadora elige un número secreto entre 1 y 10
    numero_secreto = random.randint(1, 10)
    intentos = 0
    adivinado = False

    print("¡Bienvenido al juego de adivinanzas!")
    print("Estoy pensando en un número entre 1 y 10. ¿Puedes adivinarlo?")

    # El juego continúa mientras el jugador no haya adivinado
    while not adivinado:
        # Le pedimos un número al usuario
        intento = int(input("Introduce tu número: "))
        intentos += 1

        if intento == numero_secreto:
            print(f"¡Felicidades! Lo lograste en {intentos} intentos.")
            adivinado = True
        elif intento < numero_secreto:
            print("Demasiado bajo. ¡Intenta otra vez!")
        else:
            print("Demasiado alto. ¡Intenta otra vez!")

# Esta línea inicia el juego
jugar()
