# -*- coding: utf-8 -*-
"""
Universidad del Valle de Guatemala
Matemática Discreta
Proyecto Criptografía
Pablo Sebastián Herrera & Sofia Lam Méndez
"""
#este codigo utiliza las librerias de python para encriptar y desencriptar mensajes
from cryptography.fernet import Fernet

def genera_clave():
    clave = Fernet.generate_key()
    with open("clave.key","wb") as archivo_clave:
        archivo_clave.write(clave)
        
def cargar_clave():
    return open("clave.key","rb").read()

genera_clave()
clave = cargar_clave()

mensaje = input("Ingresa el mensaje a encriptar\n").encode()
f = Fernet(clave)

encriptado = f.encrypt(mensaje)
print("\nSu mensaje Encriptado es:")
print(encriptado,"\n")

print("Su mensaje desencriptado es:")
desencriptado = f.decrypt(encriptado)
print(desencriptado)