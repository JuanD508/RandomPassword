import random 
caract ="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
canti = int(input("Digita cuantas contraseñas quieres crear / "))
password = ""
for i in range(canti):
    count = i = i + 1
    long = int(input("Digite la longitud de la contraseña / "))
    print("contraseña", count)
    for i in range(long):
        password += random.choice(caract)
    print(password)
