def main():
    # escribe tu código abajo de esta línea
    mensajes = (int(input("Dame el número de mensajes: "))) * 0.8
    megas = (float(input("Dame el número de megas: "))) * 0.8
    minutos = (int(input("Dame el número de minutos: "))) * 0.8
    costo = mensajes + megas + minutos

    print("El costo mensual es:", costo)


if __name__ == '__main__':
    main()
