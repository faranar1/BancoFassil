import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1600, 900))
fuente_tit = pygame.font.SysFont("Consolas", 45, bold=True)
fuente_opc = pygame.font.SysFont("Consolas", 30)

pins = []
money = []
moneydollars = []
moneyeuros = []
moneypounds = []

logo=pygame.image.load("difissil.jpg")


def draw_text(texto, x, y, fuente, color=(255, 255, 255)):
    img = fuente.render(str(texto), True, color)
    screen.blit(img, (x, y))

def create_pin_pygame():
    startmoney = 0
    pin_ingresado = ""
    while True:
        screen.fill((30, 30, 30))
        draw_text("CREAR PIN DE 4 DIGITOS", 600, 200, fuente_tit, (255, 255, 0))
        draw_text("NUEVO PIN: " + "*" * len(pin_ingresado), 650, 400, fuente_opc)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE: pin_ingresado = pin_ingresado[:-1]
                elif event.unicode.isdigit() and len(pin_ingresado) < 4: pin_ingresado += event.unicode
                elif event.key == pygame.K_RETURN and len(pin_ingresado) == 4:
                    if pin_ingresado not in pins:
                        pins.append(pin_ingresado)
                        money.append(startmoney)
                        moneydollars.append(startmoney)
                        moneyeuros.append(startmoney)
                        moneypounds.append(startmoney)
                        return pin_ingresado
                    else: pin_ingresado = ""

def login_pin_pygame():
    loginpin = ""
    while True:
        screen.fill((20, 20, 20))
        draw_text("INGRESA TU PIN", 650, 200, fuente_tit)
        draw_text("PIN: " + "*" * len(loginpin), 750, 400, fuente_opc)
        draw_text("Presiona (C) para crear cuenta", 600, 600, fuente_opc, (150, 150, 150))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c: return "CREAR"
                if event.key == pygame.K_BACKSPACE: loginpin = loginpin[:-1]
                elif event.unicode.isdigit() and len(loginpin) < 4: loginpin += event.unicode
                elif event.key == pygame.K_RETURN:
                    if loginpin in pins: return loginpin
                    else: loginpin = ""

def show_menu_pygame(currentpin):
    index = pins.index(currentpin)
    while True:
        screen.fill((0, 0, 0))
        draw_text("¡BIENVENIDO AL BANCO DIFISSIL!", 450, 50, fuente_tit, (0, 255, 150))
        
        screen.blit(logo, (500, 150))
        
        draw_text(f"Bolivianos: {money[index]}", 100, 200, fuente_opc, (255, 255, 255))
        draw_text(f"Dolares:    {moneydollars[index]}", 100, 250, fuente_opc, (255, 255, 255))
        draw_text(f"Euros:      {moneyeuros[index]}", 100, 300, fuente_opc, (255, 255, 255))
        draw_text(f"Libras:     {moneypounds[index]}", 100, 350, fuente_opc, (255, 255, 255))
        
        draw_text("1. DEPOSITAR / RETIRAR", 600, 450, fuente_opc)
        draw_text("2. TRANSFERENCIA", 600, 500, fuente_opc)
        draw_text("3. SALIR", 600, 550, fuente_opc, (255, 0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1: return "OP"
                if event.key == pygame.K_2: return "TR"
                if event.key == pygame.K_3: 
                    return "OUT"
def main():
    while True:
        pin_activo = login_pin_pygame()
        if pin_activo == "CREAR": pin_activo = create_pin_pygame()
        
        while True:
            index = pins.index(pin_activo)
            accion = show_menu_pygame(pin_activo)
            
            saldos_dict = {
                "Bolivianos": money[index],
                "Dolares": moneydollars[index],
                "Euros": moneyeuros[index],
                "Libras": moneypounds[index]
            }

            if accion == "OP":
                from operaciones_pygame import operaciones
                operaciones(screen, saldos_dict)
            elif accion == "TR":
                from transferencia_pygame import abrir_transferencia_pygame
                abrir_transferencia_pygame(screen, saldos_dict)
            elif accion == "OUT":
                return "OUT"

            money[index] = saldos_dict["Bolivianos"]
            moneydollars[index] = saldos_dict["Dolares"]
            moneyeuros[index] = saldos_dict["Euros"]
            moneypounds[index] = saldos_dict["Libras"]

