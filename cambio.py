tipos_de_cambio = {
	"Bolivianos": 1.0,
	"Dolares":    0.1449,
	"Euros":      0.1335,
	"Libras":     0.1142,
}


def transferir(saldos):
	print("\n====== TRANSFERENCIA ======")
	print("1. Bolivianos  saldo:", saldos["Bolivianos"])
	print("2. Dolares     saldo:", saldos["Dolares"])
	print("3. Euros       saldo:", saldos["Euros"])
	print("4. Libras      saldo:", saldos["Libras"])

	cuentas_lista = ["Bolivianos", "Dolares", "Euros", "Libras"]

	texto_origen = input("\nDe que cuenta quiere sacar el dinero? (1-4): ").strip()
	if not texto_origen.isdigit():
		print("Error: debe ingresar un numero, no letras ni simbolos")
		return saldos
	if int(texto_origen) < 1 or int(texto_origen) > 4:
		print("Error: la opcion debe ser 1, 2, 3 o 4")
		return saldos
	origen = cuentas_lista[int(texto_origen) - 1]

	texto_destino = input("A que cuenta quiere enviar el dinero? (1-4): ").strip()
	if not texto_destino.isdigit():
		print("Error: debe ingresar un numero, no letras ni simbolos")
		return saldos
	if int(texto_destino) < 1 or int(texto_destino) > 4:
		print("Error: la opcion debe ser 1, 2, 3 o 4")
		return saldos
	destino = cuentas_lista[int(texto_destino) - 1]

	if origen == destino:
		print("Error: no puede transferir a la misma cuenta")
		return saldos

	texto_monto = input(f"Cuanto quiere transferir desde {origen}? (solo numeros enteros): ").strip()
	if not texto_monto.isdigit():
		print("Error: debe ingresar un numero entero, no letras ni simbolos")
		return saldos
	monto = int(texto_monto)

	if monto == 0:
		print("Error: el monto no puede ser cero")
		return saldos
	if monto < 0:
		print("Error: el monto no puede ser negativo, ingrese un numero positivo")
		return saldos
	if monto > saldos[origen]:
		print(f"Error: saldo insuficiente en {origen}")
		print(f"Su saldo actual es {saldos[origen]} y quiere transferir {monto}")
		return saldos

	monto_en_bs = monto / tipos_de_cambio[origen]
	monto_destino = round(monto_en_bs * tipos_de_cambio[destino], 2)

	saldos[origen] = round(saldos[origen] - monto, 2)
	saldos[destino] = round(saldos[destino] + monto_destino, 2)

	print(f"\nTransferencia exitosa!")
	print(f"Se descontaron {monto} de {origen}")
	print(f"Se acreditaron {monto_destino} a {destino}")
	print("\n--- Saldos actualizados ---")
	print("Bolivianos:", saldos["Bolivianos"])
	print("Dolares:   ", saldos["Dolares"])
	print("Euros:     ", saldos["Euros"])
	print("Libras:    ", saldos["Libras"])
	return saldos
