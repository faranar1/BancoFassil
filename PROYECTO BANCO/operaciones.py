def depositar(saldo):
    print("\n===== DEPOSITO =====")
    print("1. Bolivianos")
    print("2. Dolares")
    print("3. Euros")
    print("4. Libras")

    # elegir cuenta
    texto_cuenta = input("Elija la cuenta (1-4): ").strip()
    if not texto_cuenta.isdigit() or int(texto_cuenta) < 1 or int(texto_cuenta) > 4:
        print("Error: ingrese un numero entre 1 y 4")
        return saldo
    cuentas_lista = ["Bolivianos", "Dolares", "Euros", "Libras"]
    cuenta_elegida = cuentas_lista[int(texto_cuenta) - 1]

    # pedir monto
    texto_monto = input(f"Cuanto desea depositar en {cuenta_elegida} (multiplos de 10): ").strip()
    if not texto_monto.isdigit():
        print("Error: ingrese solo numeros enteros")
        return saldo
    monto = int(texto_monto)

    if monto <= 0:
        print("Error: el monto debe ser mayor a 0")
        return saldo
    if monto % 10 != 0:
        print("Error: el monto debe ser multiplo de 10 (10, 20, 50, 100...)")
        return saldo

    # aplicar deposito
    saldo[cuenta_elegida] += monto
    print(f"Deposito exitoso. Nuevo saldo en {cuenta_elegida}: {saldo[cuenta_elegida]}")
    return saldo


def retirar(saldo):
    print("\n===== RETIRO =====")
    print("1. Bolivianos")
    print("2. Dolares")
    print("3. Euros")
    print("4. Libras")

    # elegir cuenta
    texto_cuenta = input("Elija la cuenta (1-4): ").strip()
    if not texto_cuenta.isdigit() or int(texto_cuenta) < 1 or int(texto_cuenta) > 4:
        print("Error: ingrese un numero entre 1 y 4")
        return saldo
    cuentas_lista = ["Bolivianos", "Dolares", "Euros", "Libras"]
    cuenta_elegida = cuentas_lista[int(texto_cuenta) - 1]

    # pedir monto
    texto_monto = input(f"Cuanto desea retirar de {cuenta_elegida} (multiplos de 10): ").strip()
    if not texto_monto.isdigit():
        print("Error: ingrese solo numeros enteros")
        return saldo
    monto = int(texto_monto)

    if monto <= 0:
        print("Error: el monto debe ser mayor a 0")
        return saldo
    if monto % 10 != 0:
        print("Error: el monto debe ser multiplo de 10 (10, 20, 50, 100...)")
        return saldo
    if monto > saldo[cuenta_elegida]:
        print(f"Error: saldo insuficiente en {cuenta_elegida}")
        print(f"Su saldo actual es {saldo[cuenta_elegida]} y quiere retirar {monto}")
        return saldo

    # aplicar retiro
    saldo[cuenta_elegida] -= monto
    print(f"Retiro exitoso. Nuevo saldo en {cuenta_elegida}: {saldo[cuenta_elegida]}")
    return saldo
