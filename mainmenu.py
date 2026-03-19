
numeros="0123456789"

#

pins=[]
money=[]
moneydollars=[]
moneyeuros=[]
moneypounds=[]
indice=len(pins)

#se crea un usuario nuevo si al verificar
def create_pin(pins, money):
    startmoney=0
    
    print("Crear pin de 4 digitos")
    while True:
        
        pin=input("Ingresa un pin: ")
        if len(pin)==4:
            
            if type(pin)==int:
                pinvalido=True
            elif pin in pins:
                    print("Pin ya existe")
            else: print("Pin invalido")
            
            

            
        else: print("pin invalido")
        if pinvalido==True:
            
            pins.append(pin)
            money.append(startmoney)
            moneydollars.append(startmoney)
            moneyeuros.append(startmoney)
            moneypounds.append(startmoney)
            return pins, money, moneydollars, moneyeuros, moneypounds
        

def login_pin(pins):
    while True:
        
        loginpin=input("Ingresa tu pin: ")

        if loginpin in pins:
            return loginpin
        else: 
            print("Pin invalido")
            print("Crear cuenta?")
            
            eleccion=input("Escribe (y) si quieres crear cuenta, sino introduce lo que sea: ")
            if eleccion!="y":
                continue
            
            loginpin=create_pin(pins,money)
            if loginpin in pins:
                return loginpin
    
        




pin=login_pin(pins)

def show_menu(currentpin,pins):
    print("|||||||||||¡Bienvenido al Banco Difissil!|||||||||||")
    index=pins.index(pin)
    opcion=0
    while True:
        while opcion not in [1,2,3,4,5]:
        
            print("Bolivianos: ",money[index])
            print("Dolares: ",moneydollars[index])
            print("Euros: ",moneyeuros[index])
            print("Libras Esterlinas: ",moneypounds[index])
            print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
            print("         Opciones:")
            print("   1.  Depositar")
            print("   2.  Retiro")
            print("   3.  Transferencia")
            print("   4.  Conversion de moneda")
            print("   5.  Salir")
            print("/////////////////////////////////////////////////////////////")
            opcion=input("Ingresa una opción: ")
            try: opcion=int(opcion)
            except: continue
            if opcion==1:
                True
            if opcion==2:
                True
            if opcion==3:
                True
            if opcion==4:
                True
            if opcion==5:
                False
                
