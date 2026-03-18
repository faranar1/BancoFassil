def depositar(saldo):
	while True:
		deposito = float(input("\nIngrese el monto a depositar: "))
		if deposito > 0:
			saldo += deposito
			print (f"Deposito exitoso. Nuevo saldo: {saldo}")
			return saldo
		else:
			print ("Error: El monto debe ser positvo.")

def retirar(saldo):
	while True:
		retiro = float(input("\nIngrese el monto a retirar: "))
		if retiro < 0:
			print("Error: El monto debe ser positvo.")
		elif retiro > saldo:
			print(f"Error: Fondos insuficientes. Tu saldo es {saldo}")
			return saldo
		else:
			saldo-= retiro
			print(f"Retiro exitoso. Nuevo saldo: {saldo}")
			return saldo


def consultar(saldo):
	print("\n================")
	print(f"Saldo actual: {saldo}")
	print("================")



saldo = 0
ejecutando = True

while ejecutando:
	print("\n---- Menu Cajero ----")
	print("1. Consultar Saldo")
	print("2. Depositar Dinero")
	print("3. Retirar Dinero")
	print("4. Salir")

	opcion = input("Elija una opcion: ")

	if opcion == "1":
		consultar(saldo)
	elif opcion == "2":
		saldo = depositar(saldo)
	elif opcion == "3":
		saldo = retirar(saldo)
	elif opcion == "4":
		print("\nGracias por usar el cajero, vuelva pronto.")
		ejecutando = False
	else:
		print("Opcion no valida, intente de nuevo.")
