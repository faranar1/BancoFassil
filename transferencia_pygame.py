import pygame
from transferencia import tipos_de_cambio

# estas variables solo se usan cuando el archivo corre solo para probar
# cuando Franco importe este archivo NO se van a ejecutar
cuentas_lista = ["Bolivianos", "Dolares", "Euros", "Libras"]

def abrir_transferencia_pygame(screen, saldos):
    fuente        = pygame.font.SysFont("Consolas", 24)
    fuente_titulo = pygame.font.SysFont("Consolas", 32, bold=True)
    clock         = pygame.time.Clock()  # controla los fps para no consumir 100% CPU

    origen      = None
    destino     = None
    monto_texto = ""
    mensaje     = ""

    while True:
        screen.fill((13, 27, 42))

        # titulo
        screen.blit(fuente_titulo.render("====== TRANSFERENCIA ======", True, (2, 195, 154)), (550, 40))

        # cuentas con saldo
        for i, cuenta in enumerate(cuentas_lista):
            screen.blit(fuente.render(f"{i+1}. {cuenta}: {saldos[cuenta]}", True, (255, 255, 255)), (550, 130 + i * 50))

        # instruccion segun lo que falta
        if not origen:
            inst = "Elige cuenta ORIGEN (1-4)  |  0 = volver"
        elif not destino:
            inst = "Elige cuenta DESTINO (1-4)  |  0 = volver"
        else:
            inst = f"Origen: {origen}  Destino: {destino}  |  Escribe monto + ENTER  |  0 = volver"
        screen.blit(fuente.render(inst, True, (246, 201, 14)), (400, 360))

        # monto que va escribiendo
        if origen and destino:
            screen.blit(fuente.render(f"Monto: {monto_texto}_", True, (255, 255, 255)), (550, 420))

        # mensaje verde si exitoso, rojo si error
        if mensaje:
            color = (2, 195, 154) if "exitosa" in mensaje else (255, 100, 100)
            screen.blit(fuente.render(mensaje, True, color), (500, 500))

        pygame.display.flip()
        clock.tick(60)  # limita a 60 fps para no consumir todo el procesador

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return saldos

            if event.type == pygame.KEYDOWN:

                # cancelar con 0 solo si no hay monto escrito
                if event.key == pygame.K_0 and monto_texto == "":
                    return saldos

                # elegir origen
                elif not origen and event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                    origen  = cuentas_lista[int(event.unicode) - 1]
                    mensaje = ""

                # elegir destino
                elif origen and not destino and event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                    destino = cuentas_lista[int(event.unicode) - 1]
                    if origen == destino:
                        mensaje = "Error: no puede elegir la misma cuenta"
                        destino = None  # solo resetea destino, origen se mantiene
                    else:
                        mensaje = ""

                # escribir monto
                elif origen and destino:
                    if event.key == pygame.K_BACKSPACE:
                        monto_texto = monto_texto[:-1]
                    elif event.unicode.isdigit():
                        monto_texto += event.unicode
                    elif event.key == pygame.K_RETURN:
                        if not monto_texto or int(monto_texto) == 0:
                            mensaje     = "Error: ingrese un monto valido"
                            monto_texto = ""
                        elif int(monto_texto) > saldos[origen]:
                            mensaje     = f"Error: saldo insuficiente. Tiene {saldos[origen]}"
                            monto_texto = ""
                        else:
                            monto         = int(monto_texto)
                            monto_destino = round((monto / tipos_de_cambio[origen]) * tipos_de_cambio[destino], 2)
                            saldos[origen]  = round(saldos[origen]  - monto, 2)
                            saldos[destino] = round(saldos[destino] + monto_destino, 2)
                            mensaje     = f"exitosa! {monto} {origen} -> {monto_destino} {destino}"
                            monto_texto = ""
                            origen      = None
                            destino     = None

