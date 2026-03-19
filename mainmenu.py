numeros="0123456789"

pins=[]
money=[]
moneydollars=[]
moneyeuros=[]
moneypounds=[]
indice=len(pins)

def create_pin(pins, money):
    startmoney=0
    
    print("Crear pin de 4 digitos")
    while True:
        
        pin=input("Ingresa un pin: ")
        pinvalido=False
        
        if len(pin)==4:
            
            if pin.isdigit():
                if pin in pins:
                    print("Pin ya existe")
                else:
                    pinvalido=True
            else: 
                print("Pin invalido")
        else: 
            print("pin invalido")
        
        if pinvalido==True:
            pins.append(pin)
            money.append(startmoney)
            moneydollars.append(startmoney)
            moneyeuros.append(startmoney)
            moneypounds.append(startmoney)
            return pin
        

def login_pin(pins):
    while True:
        
        loginpin=input("Ingresa tu pin: ")

        if loginpin in pins:
            return loginpin
        else: 
            print("Pin invalido")
            print("Crear cuenta?")
            
            eleccion=input("Escribe (y) si quieres crear cuenta: ")
            if eleccion!="y":
                continue
            
            return create_pin(pins,money)


def show_menu(currentpin,pins):
    print("|||||||||||¡Bienvenido al Banco Difissil!|||||||||||")
    index=pins.index(currentpin)

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

    try:
        opcion=int(opcion)
    except:
        print("Opcion invalida")
        return

    print("Elegiste la opcion:", opcion)


pin=login_pin(pins)
show_menu(pin, pins)