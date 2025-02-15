import random
caract ="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
long = int(input("Digite la longitud de la contraseña"))
password = ""
for i in range(long):
    password += random.choice(caract)
print(password)
