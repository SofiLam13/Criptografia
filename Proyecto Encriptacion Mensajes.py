# -*- coding: utf-8 -*-
"""
Universidad del Valle de Guatemala
Matemática Discreta
Proyecto Criptografía
Pablo Sebastián Herrera & Sofia Lam Méndez
"""
import math
print("Bienvenido al programa de encriptación de mensaje")
entry = input("Ingrese el mensaje que se encriptara\n")
Codificacion = ["*","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",0,1,2,3,4,5,6,7,8,9]
#se convierte todo el mensaje a mayusculas
#para luego encontrarlo en la codificacion
Entry = entry.upper()
#se guarda el mensaje en una lista para poder compararla en la codificacion
Mensaje = list(Entry)
#se crea una lista que guardara las representaciones
#de las letras del mensaje
Coded_message_list = []
#se recorre la lista Mensaje, por cada elemento de esa lista
#se obtiene la representacion de la letra y se almacena en Coded_message
for caracter in Mensaje:
    if caracter in Codificacion:
        Coded_message_list.append(Codificacion.index(caracter))
#Se le pide al usuario los números con los que se desea encriptar el menaje

p=int(input("Por favor ingrese un número primo"))
q=int(input("Por favor ingrese un número primo diferente al anterior"))
n=p*q
fi=(p-1)*(q-1)
print("Ahora necesitamos de una llave para la codificación del mensaje, recuerde el número", fi)
e=int(input("Por favor ingrese un número que sea primo relativo del número anteriormente mostrado"))
if math.gcd(fi,e)==1:
    print("Llave aceptada")
else:
    print("Por favor ingresar un primo relativo al número dado")

print("Su llave pública es: (", n ,",", e, ")")
d=0
x=0
#Se crea una función para encontrar el entero d que codificará todo el mensaje
#Se resuelve como una ecuación diofántica (?)
# e * d equivale a 1 en el módulo fi
def calculandoD():
    #(e*d)-(fi*x)=1
    return d