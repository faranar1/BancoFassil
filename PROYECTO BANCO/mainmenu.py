import operaciones
import transferencia
import os

# listas donde se guardan los datos de cada cuenta
pins        = []
bolivianos  = []
dolares     = []
euros       = []
libras      = []
def limpiar():
	os.system("cls" if os.name == "nt" else "clear")
	#os.system lo que hace es que ejecuta lo que esta dentro como si fuera escrito
	#en la terminal
	#basicamente lo que dice adentro es ejecuta 'cls' si el nombre del sistema es nt
	#windows retorna nt como su nombre
	#si no, ejecuta clear
	#ambas formas hace que se limpie la pantalla


def crear_cuenta():
	limpiar()
	print("\n===== CREAR CUENTA =====")
	print("El pin debe tener exactamente 4 digitos numericos")

	while True:
		pin = input("Ingresa un pin de 4 digitos: ").strip()

		if not pin.isdigit():
			print("Error: el pin solo puede tener numeros")
			continue
		if len(pin) != 4:
			print("Error: el pin debe tener exactamente 4 digitos")
			continue
		if pin in pins:
			print("Error: ese pin ya existe, elige otro")
			continue

		# guardar la cuenta con saldo inicial 0 en todas las monedas
		pins.append(pin)
		bolivianos.append(0)
		dolares.append(0)
		euros.append(0)
		libras.append(0)
		print(f"\nCuenta creada exitosamente! Tu pin es: {pin}")
		return pin


def iniciar_sesion():
	limpiar()
	print("\n===== INICIAR SESION =====")
	intentos = 0

	while intentos < 3:
		pin = input("Ingresa tu pin: ").strip()

		if pin in pins:
			print(f"\nBienvenido!")
			return pin
		else:
			intentos += 1
			restantes = 3 - intentos
			if restantes > 0:
				print(f"Pin incorrecto. Intentos restantes: {restantes}")
			else:
				print("Demasiados intentos fallidos.")

	return None


def get_saldos(index):
	# convierte las listas a un diccionario para pasarlo a operaciones y transferencia
	return {
		"Bolivianos": bolivianos[index],
		"Dolares":    dolares[index],
		"Euros":      euros[index],
		"Libras":     libras[index],
	}


def set_saldos(index, saldos):
	# guarda de vuelta el diccionario actualizado en las listas
	bolivianos[index] = saldos["Bolivianos"]
	dolares[index]    = saldos["Dolares"]
	euros[index]      = saldos["Euros"]
	libras[index]     = saldos["Libras"]


def mostrar_saldos(index):
	print("\n===== CONSULTA DE SALDO =====")
	print(f"Bolivianos: {bolivianos[index]}")
	print(f"Dolares:    {dolares[index]}")
	print(f"Euros:      {euros[index]}")
	print(f"Libras:     {libras[index]}")


def menu_banco(pin):
	index = pins.index(pin)

	while True:
		limpiar()
		print("\n||||| BANCO DIFISSIL |||||")
		print(f"Bolivianos: {bolivianos[index]}")
		print(f"Dolares:    {dolares[index]}")
		print(f"Euros:      {euros[index]}")
		print(f"Libras:     {libras[index]}")
		print("==========================")
		print("1. Depositar")
		print("2. Retirar")
		print("3. Transferencia entre cuentas")
		print("4. Consultar saldo")
		print("5. Salir")
		print("==========================")

		opcion = input("Ingresa una opcion: ").strip()

		if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
			print("Error: ingrese un numero entre 1 y 5")
			input("\nPresiona Enter para continuar...")
			continue

		opcion = int(opcion)

		if opcion == 1:
			saldos = get_saldos(index)
			saldos = operaciones.depositar(saldos)
			set_saldos(index, saldos)
			input("\nPresiona Enter para continuar...")

		elif opcion == 2:
			saldos = get_saldos(index)
			saldos = operaciones.retirar(saldos)
			set_saldos(index, saldos)
			input("\nPresiona Enter para continuar...")

		elif opcion == 3:
			saldos = get_saldos(index)
			saldos = transferencia.transferir(saldos)
			set_saldos(index, saldos)
			input("\nPresiona Enter para continuar...")
			
		elif opcion == 4:
			mostrar_saldos(index)
			input("\nPresiona Enter para continuar...")

		elif opcion == 5:
			print("\nGracias por usar el Banco Difissil. Hasta luego!")
			break


#PROGRAMA PRINCIPAL
print("================================")
print("   Bienvenido al Banco Difissil")
print("================================")

while True:
	print("\n1. Iniciar sesion")
	print("2. Crear cuenta")
	print("3. Salir")

	opcion = input("\nIngresa una opcion: ").strip()

	if opcion == "1":
		pin_activo = iniciar_sesion()
		if pin_activo is not None:
			menu_banco(pin_activo)

	elif opcion == "2":
		pin_activo = crear_cuenta()
		if pin_activo is not None:
			menu_banco(pin_activo)

	elif opcion == "3":
		print("Hasta luego!")
		break

	else:
		print("Error: ingrese 1, 2 o 3")
