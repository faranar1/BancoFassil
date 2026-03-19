def procesar_deposito(saldo, cuenta_elegida, deposito_usuario):
	if not deposito_usuario.isdigit():
		return saldo, "Error: Ingrese solo numeros."

	deposito = int(deposito_usuario)

	if deposito <= 0:
		return saldo, "Error: El monto debe ser mayor a 0."
	if deposito % 10 != 0:
		return saldo, "Error: Solo multiplos de 10."

	saldo[cuenta_elegida] += deposito
	return saldo, f"Deposito exitoso en {cuenta_elegida}"


def procesar_retiro(saldo, cuenta_elegida, retiro_usuario):
	if not retiro_usuario.isdigit():
		return saldo, "Error: Ingrese solo numeros."

	retiro = int(retiro_usuario)

	if retiro <= 0:
		return saldo, "Error: El monto debe ser mayor a 0."
	if retiro % 10 != 0:
		return saldo, "Error: Solo multiplos de 10."
	if retiro > saldo[cuenta_elegida]:
		return saldo, f"Error: Saldo insuficiente en {cuenta_elegida}."

	saldo[cuenta_elegida] -= retiro

	return saldo, f"Retiro exitoso de {cuenta_elegida}"