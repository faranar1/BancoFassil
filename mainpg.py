import pygame
clock = pygame.time.Clock()
running=True
screen = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("Banco Difissil") 
menu_login=True
from mainmenupg import create_pin_pygame, login_pin_pygame, show_menu_pygame, pins, money, moneydollars, moneyeuros, moneypounds
from operaciones_pygame import operaciones
from transferencia_pygame import abrir_transferencia_pygame
import sys


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pin_activo=login_pin_pygame()

    if pin_activo=="CREAR":
        pin_activo=create_pin_pygame()
    
    activesession= True
    while activesession:
        index=pins.index(pin_activo)
        action=show_menu_pygame(pin_activo)

        saldos_dict={
            "Bolivianos": money[index],
            "Dolares": moneydollars[index],
            "Euros": moneyeuros[index],
            "Libras": moneypounds[index]
        }
        if action=="OP":
            operaciones(screen, saldos_dict)
        elif action=="TR":
            saldos_dict=abrir_transferencia_pygame(screen, saldos_dict)
        elif action=="OUT":
            activesession=False
        money[index]=saldos_dict["Bolivianos"]
        moneydollars[index]=saldos_dict["Dolares"]
        moneyeuros[index]=saldos_dict["Euros"]
        moneypounds[index]=saldos_dict["Libras"]
        

   
    pygame.display.flip()
    clock.tick(120)