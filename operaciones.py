def depositar(saldo):
	print("\n===== DEPOSITO =====")
	print("1. Bolivianos\n2. Dolares\n3. Euros\n4. Libras")
	
	texto_cuenta = input("Elija la cuenta (1-4): ").strip()
	
	if not texto_cuenta.isdigit() or int(texto_cuenta) < 1 or int(texto_cuenta) > 4:
		print("Opcion no valida")
		return saldo
	cuentas_lista = ['Bolivianos', 'Dolares', 'Euros', 'Libras']
	cuenta_elegida = cuentas_lista[int(texto_cuenta) - 1]

	deposito_usuario = input(f"Cuanto desea depositar en {cuenta_elegida}: ").strip()

	if not deposito_usuario.isdigit():
		print("Error: Por favor, ingrese solo numeros.")
		return saldo

	deposito = int(deposito_usuario)

	if deposito <= 0:
		print("El monto debe ser mayor a 0")
	elif deposito % 10 != 0:
		print("El monto debe ser multiplo de 10")
	else:
		saldo[cuentas_elegida] += deposito
		print (f"Deposito exitoso. Nuevo saldo en {cuenta_elegida}: {saldo[cuentas_elegida]}")
	return saldo	



def retirar(saldo):
	print("\n====== RETIRO =====")
	print("1. Bolivianos\n2. Dolares\n3. Euros\n4. Libras")

	texto_cuenta = input("Elija la cuenta (1-4): ").strip()

	if not texto_cuenta.isdigit() or int(texto_cuenta) < 1 or int(texto_cuenta) > 4:
		print("Opcion no valida")
		return saldo
	cuentas_lista = ['Bolivianos', 'Dolares', 'Euros', 'Libras']
	cuenta_elegida = cuentas_lista[int(texto_cuenta) - 1]

	retiro_usuario = input(f"Cuanto desea retirar en {cuenta_elegida}: ").strip()

	if not deposito_usuario.isdigit():
		print("Error: Por favor, ingrese solo numeros.")
		return saldo

	retiro = int(retiro_usuario)

	if retiro <= 0:
		print("El monto debe ser mayor a 0")
	elif retiro % 10 != 0:
		print("El monto debe ser multiplo de 10")
	elif retiro > saldo[cuentas_elegida]:
		print(f"Saldo insuficienteen {cuenta_elegida}. Saldo actual: {saldo[cuentas_elegida]}")
	else:
		saldo[cuentas_elegida] -= retiro
		print (f"Retiro exitoso. Nuevo saldo en {cuenta_elegida}: {saldo[cuentas_elegida]}")
	return saldo	
