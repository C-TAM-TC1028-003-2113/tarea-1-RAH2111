import math


def main():
    # escribe tu código abajo de esta línea
    palabras = int(input("Dame el número de palabras: "))
    paginas = math.ceil(palabras / 475)

    print("El costo de la publicación es:", paginas * 60 * 0.9)


if __name__ == '__main__':
    main()
