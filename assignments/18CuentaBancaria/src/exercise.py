def main():
    # escribe tu código abajo de esta línea
    saldo = float(input('Dame el saldo del mes anterior: ')) * 0.925
    ingresos = float(input('Dame los ingresos: '))
    egresos = float(input('Dame los egresos: '))
    cheques = int(input('Dame el número de cheques: '))

    saldo_final = saldo + ingresos - egresos - cheques * 13

    print('El saldo final de la cuenta es: ', saldo_final)


if __name__ == '__main__':
    main()
