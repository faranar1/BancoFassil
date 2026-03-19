import pygame
from operacionespygame import procesar_deposito, procesar_retiro

pygame.init()
screen = pygame.display.set_mode((1600,900))
pygame.display.set_caption("Operaciones")


def operaciones(screen, saldos_usuario,modo):
	running=True

	modo = modo
	monto_acumulado = ""
	cuenta_seleccionada = None
	nombres_cuentas = ["Bolivianos", "Dolares", "Euros", "Libras"]
	mensaje_estado = ""


	fuente_titulo = pygame.font.SysFont("Consolas", 40, bold =True)
	fuente_media = pygame.font.SysFont("Consolas", 28, bold =True)
	fuente_peque = pygame.font.SysFont("Consolas", 23)
	fuente_numero = pygame.font.SysFont("Consolas", 25,bold=True)

	screen.fill((0,0,0))

	def deposito():
		pygame.draw.rect(screen,(40,40,40),(450,50,700,790))
		pygame.draw.rect(screen,(222,222,222), (500,340, 590,60))
		txt_monto = fuente_numero.render(monto_acumulado, True, (0,0,0))
		screen.blit(txt_monto, (510,355))
		pygame.draw.rect(screen, (0,150,0), rect_confirmar)
		txt_conf = fuente_media.render("CONFIRMAR", True, (255,255,255))
		screen.blit(txt_conf, (890,765))

		pygame.draw.rect(screen,(200,0,0),rect_salir, border_radius=5)
		txto_salir = fuente_peque.render("SALIR", True, (255,255,255))
		screen.blit(txto_salir,(985,90))

		pygame.draw.rect(screen, (133,133,133), (650,450, 50,50))
		pygame.draw.rect(screen, (133,133,133), (750,450, 50,50))
		pygame.draw.rect(screen, (133,133,133), (850,450, 50,50))

		pygame.draw.rect(screen, (133,133,133), (650,550, 50,50))
		pygame.draw.rect(screen, (133,133,133), (750,550, 50,50))
		pygame.draw.rect(screen, (133,133,133), (850,550, 50,50))

		pygame.draw.rect(screen, (133,133,133), (650,650, 50,50))
		pygame.draw.rect(screen, (133,133,133), (750,650, 50,50))
		pygame.draw.rect(screen, (133,133,133), (850,650, 50,50))

		pygame.draw.rect(screen, (133,133,133), (750,750, 50,50))

		titulo = fuente_titulo.render("DEPOSITO",True,(158,158,158))
		texto_monto = fuente_media.render("Monto a depositar:", True, (158,158,158))
		texto_cuenta = fuente_peque.render("Elija la cuenta (1-4)", True, (158,158,158))
		texto_cuentas = fuente_peque.render("[1] Bolivianos [2] Dolares [3] Euros [4] Libras", True, (158,158,158))

		numero_1 = fuente_numero.render("1", True, (255,255,255))
		numero_2 = fuente_numero.render("2", True, (255,255,255))
		numero_3 = fuente_numero.render("3", True, (255,255,255))
		numero_4 = fuente_numero.render("4", True, (255,255,255))
		numero_5 = fuente_numero.render("5", True, (255,255,255))
		numero_6 = fuente_numero.render("6", True, (255,255,255))
		numero_7 = fuente_numero.render("7", True, (255,255,255))
		numero_8 = fuente_numero.render("8", True, (255,255,255))
		numero_9 = fuente_numero.render("9", True, (255,255,255))
		numero_0 = fuente_numero.render("0", True, (255,255,255))

		screen.blit(titulo,(700, 80))
		screen.blit(texto_monto,(500, 290))
		screen.blit(texto_cuenta,(500, 130))
		screen.blit(texto_cuentas, (500, 180))


		screen.blit(numero_1, (665,460))
		screen.blit(numero_2, (765,460))
		screen.blit(numero_3, (865,460))

		screen.blit(numero_4, (665,560))
		screen.blit(numero_5, (765,560))
		screen.blit(numero_6, (865,560))

		screen.blit(numero_7, (665,660))
		screen.blit(numero_8, (765,660))
		screen.blit(numero_9, (865,660))

		screen.blit(numero_0, (765,760))

		if mensaje_estado:
			color_texto = (255,0,0) if "Error" in mensaje_estado else (0,255,0)
			aviso = fuente_peque.render(mensaje_estado, True, color_texto)
			screen.blit(aviso,(500,415))
		if cuenta_seleccionada:
			txto_selec = fuente_peque.render(f"Cuenta: {cuenta_seleccionada}",True, (255,255,255))
			screen.blit(txto_selec, (500,220))

	def retiro():
		pygame.draw.rect(screen,(40,40,40),(450,50,700,790))
		pygame.draw.rect(screen,(222,222,222), (500,340, 590,60))

		txt_monto = fuente_numero.render(monto_acumulado, True, (0,0,0))
		screen.blit(txt_monto, (510,355))
		pygame.draw.rect(screen, (0,150,0), rect_confirmar)
		txt_conf = fuente_media.render("CONFIRMAR", True, (255,255,255))
		screen.blit(txt_conf, (890,765))

		pygame.draw.rect(screen,(200,0,0),rect_salir, border_radius=5)
		txto_salir = fuente_peque.render("SALIR", True, (255,255,255))
		screen.blit(txto_salir,(985,90))

		
		pygame.draw.rect(screen, (133,133,133), (650,450, 50,50))
		pygame.draw.rect(screen, (133,133,133), (750,450, 50,50))
		pygame.draw.rect(screen, (133,133,133), (850,450, 50,50))

		pygame.draw.rect(screen, (133,133,133), (650,550, 50,50))
		pygame.draw.rect(screen, (133,133,133), (750,550, 50,50))
		pygame.draw.rect(screen, (133,133,133), (850,550, 50,50))

		pygame.draw.rect(screen, (133,133,133), (650,650, 50,50))
		pygame.draw.rect(screen, (133,133,133), (750,650, 50,50))
		pygame.draw.rect(screen, (133,133,133), (850,650, 50,50))

		pygame.draw.rect(screen, (133,133,133), (750,750, 50,50))

		titulo = fuente_titulo.render("RETIRO",True,(158,158,158))
		texto_monto = fuente_media.render("Monto a retirar:", True, (158,158,158))
		texto_cuenta = fuente_peque.render("Elija la cuenta (1-4)", True, (158,158,158))
		texto_cuentas = fuente_peque.render("[1] Bolivianos [2] Dolares [3] Euros [4] Libras", True, (158,158,158))

		numero_1 = fuente_numero.render("1", True, (255,255,255))
		numero_2 = fuente_numero.render("2", True, (255,255,255))
		numero_3 = fuente_numero.render("3", True, (255,255,255))
		numero_4 = fuente_numero.render("4", True, (255,255,255))
		numero_5 = fuente_numero.render("5", True, (255,255,255))
		numero_6 = fuente_numero.render("6", True, (255,255,255))
		numero_7 = fuente_numero.render("7", True, (255,255,255))
		numero_8 = fuente_numero.render("8", True, (255,255,255))
		numero_9 = fuente_numero.render("9", True, (255,255,255))
		numero_0 = fuente_numero.render("0", True, (255,255,255))

		screen.blit(titulo,(700, 80))
		screen.blit(texto_monto,(500, 290))
		screen.blit(texto_cuenta,(500, 130))
		screen.blit(texto_cuentas, (500, 180))

		screen.blit(numero_1, (665,460))
		screen.blit(numero_2, (765,460))
		screen.blit(numero_3, (865,460))

		screen.blit(numero_4, (665,560))
		screen.blit(numero_5, (765,560))
		screen.blit(numero_6, (865,560))

		screen.blit(numero_7, (665,660))
		screen.blit(numero_8, (765,660))
		screen.blit(numero_9, (865,660))

		screen.blit(numero_0, (765,760))

		if mensaje_estado:
			color_texto = (255,0,0) if "Error" in mensaje_estado else (0,255,0)
			aviso = fuente_peque.render(mensaje_estado, True, color_texto)
			screen.blit(aviso,(500,415))
		if cuenta_seleccionada:
			txto_selec = fuente_peque.render(f"Cuenta: {cuenta_seleccionada}",True, (255,255,255))
			screen.blit(txto_selec, (500,220))


	rect_confirmar = pygame.Rect(880, 750, 160, 60)
	rect_salir = pygame.Rect(970,80,100,40)
	while running:
		screen.fill((0,0,0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					cuenta_seleccionada = nombres_cuentas[0]
				if event.key == pygame.K_2:
					cuenta_seleccionada = nombres_cuentas[1]
				if event.key == pygame.K_3:
					cuenta_seleccionada = nombres_cuentas[2]
				if event.key == pygame.K_4:
					cuenta_seleccionada = nombres_cuentas[3]

				if event.key == pygame.K_BACKSPACE:
					monto_acumulado = monto_acumulado[:-1]
				
			if event.type == pygame.MOUSEBUTTONDOWN:
				x, y = event.pos

				if 650 <= x <= 700 and 450 <= y <=500:
					monto_acumulado += "1"
				elif 750 <= x <= 800 and 450 <= y <= 500:
					monto_acumulado += "2"
				elif 850 <= x <=900 and 450 <= y <= 500:
					monto_acumulado += "3"

				elif 650 <= x <=700 and 550 <= y <= 600:
					monto_acumulado += "4"
				elif 750 <= x <=800 and 550 <= y <= 600:
					monto_acumulado += "5"
				elif 850 <= x <=900 and 550 <= y <= 600:
					monto_acumulado += "6"

				elif 650 <= x <=700 and 650 <= y <= 700:
					monto_acumulado += "7"
				elif 750 <= x <=800 and 650 <= y <= 700:
					monto_acumulado += "8"
				elif 850 <= x <=900 and 650 <= y <= 700:
					monto_acumulado += "9"

				elif 750 <= x <=800 and 750 <= y <= 800:
					monto_acumulado += "0"


				elif rect_confirmar.collidepoint(x,y):
					if cuenta_seleccionada and monto_acumulado!="":
						if modo == "deposito":
							saldos_usuario, mensaje_estado = procesar_deposito(saldos_usuario, cuenta_seleccionada, monto_acumulado)
						elif modo == "retiro":
							saldos_usuario, mensaje_estado = procesar_retiro(saldos_usuario, cuenta_seleccionada, monto_acumulado)
						monto_acumulado =""
					else:
						mensaje_estado = "Error: Elija cuenta y monto"
				elif rect_salir.collidepoint(x,y):
					running = False
		if modo == "deposito":
			deposito()
		elif modo == "retiro":
			retiro()
		else:
			# botones en el main que ponga modo deposito o retiro
			pass
		pygame.display.flip()
