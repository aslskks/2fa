import pyotp
import os

def archivoleer():
    if os.path.exists("key.txt"):
        leer = open("key.txt", "r")
        leeido =  leer.read()
        return leeido
    else:
        print("el archivo key.txt que contiene la llave no existe por favor usar el otro archivo para crear el archivo de key.txt y su qr para leer con el autenticator")
        exit() 
key = archivoleer()

trpo = pyotp.TOTP(key)

while True:
    print(trpo.verify(input("codigo: ")))