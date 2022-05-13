# -*- coding: utf-8 -*-
"""
Universidad del Valle de Guatemala
Matemática Discreta
Proyecto Criptografía
Pablo Sebastián Herrera & Sofia Lam Méndez
"""

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