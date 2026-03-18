vocales="aeiouAEIOU"
numeros="0123456789"

#
users=[]
passwords=[]
money=[]
moneydollars=[]
moneyeuros=[]
moneysoles=[]
indice=len(users)

#se crea un usuario nuevo si al verificar
def create_user(users, passwords, money):
    startmoney=0
    print("Ingresa un usuario y una contraseña (Solo pueden tener entre 4 y 6 caracteres, y 4 contener vocales (aeiou, AEIOU) y numeros (0123456789)")
    while True:
        print("Registro de usuario:")
        user=input("Ingresa un nombre de usuario: ")
        password=input("Ingresa una contraseña: ")
        if 4<len(user)<6:
            vocalesuser = sum(1 for char in user if char in vocales)
            numerosuser= sum(1 for char in user if char in numeros)
            if vocalesuser+numerosuser>2:
                uservalido=True
            elif user in users:
                print("Nombre ocupado")
            else: print("Usuario invalido")
            vocalespass = sum(1 for char in password if char in vocales)
            numerospass= sum(1 for char in password if char in numeros)
            if vocalespass+numerospass>4:
                passvalido=True
            else: print("Password invalido")
            if uservalido==True and passvalido==True:
                users[indice]=user
                passwords[indice]=password
                money[indice]=startmoney
                moneydollars[indice]=startmoney
                moneyeuros[indice]=startmoney
                moneysoles[indice]=startmoney
                return users, passwords, money, moneydollars, moneyeuros, moneysoles
        break

def login_user(users, passwords):
    while True:
        loginuser=input("Ingresa tu usuario: ")
        loginpass=input("Ingresa tu contraseña: ")

        if loginuser in users and loginpass in passwords and users.index(loginuser)==passwords.index(loginpass):
            return True, loginuser, loginpass
        else: 
            print("Crear cuenta?")
            while True:
                eleccion=input("y/n: ")
                if eleccion!=y:
                    break
                else:
                    loginuser,loginpass,loginmoney=create_user(users,passwords,money)

    
        






def show_menu():
    print("|||||||||||¡Bienvenido al Banco Difissil!|||||||||||")
    while True:
        print(user)
        