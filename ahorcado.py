from operator import is_not


def mostrar_ahorcado(intentos):
    estados = [
        """
           ------
           |    |
                |
                |
                |
                |
        =========
        """,
        """
           ------
           |    |
           O    |
                |
                |
                |
        =========
        """,
        """
           ------
           |    |
           O    |
           |    |
                |
                |
        =========
        """,
        """
           ------
           |    |
           O    |
          /|    |
                |
                |
        =========
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
                |
                |
        =========
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
          /     |
                |
        =========
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
          / \\   |
                |
        =========
        """
    ]
    print(estados[intentos])
def jugar_ahorcado():
    palabra = input("Dame una plabra:")
    palabra_secreta = palabra
    palabra_mostrada = ["-" for _ in palabra_secreta]
    letras_usadas = []
    intentos = 0
    max_intentos = len(palabra_secreta)

    while intentos <= max_intentos:
        mostrar_ahorcado(intentos)

        print("Letras ya dichas:", "".join(sorted(letras_usadas)))
        print("Palabra:", "".join(palabra_mostrada))
        letra = input("Adivina una letra: ").lower()
        if not letra.isalpha() or len(letra) != 1:
            print("Por favor, introduce solo una letra válida.")
            continue
        if letra in letras_usadas:
            print("Ya dijiste esa letra.")
            continue

        letras_usadas.append(letra)

        if letra in palabra_secreta:
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                    palabra_mostrada[i] = letra
            if "-" not in palabra_mostrada:
                print("¡Felicidades! Adivinaste la palabra:", palabra_secreta)
                break
        else:
            intentos += 1

    if intentos > max_intentos:
        print("Perdiste...")
        print("La palabra era:", palabra_secreta)

    jugar_nuevo = input("¿Jugar de nuevo? (s/n): ").lower()
    if jugar_nuevo == 's':
        jugar_ahorcado()

# Inicia el juego

jugar_ahorcado()