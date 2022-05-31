# -*- coding: utf-8 -*-
"""
Universidad del Valle de Guatemala
Matemática Discreta
Proyecto Criptografía
Pablo Sebastián Herrera & Sofia Lam Méndez
"""
def is_prime(n):
    for i in range (2,n):
        if n%i == 0:
            return False
        return True
    
def ChoosePrime():
    print("Ingrese un numero primo")
    prime = int(input())
    while is_prime(prime)==False:
        print("El numero ingresado no es primo, intente de nuevo")
        prime = int(input())
    return prime

def IdenticalPrimes(p,q):
    if p==q:
        print("Los primos ingresados deben ser diferentes, intente de nuevo")
        return True
    else:
        return False
    
def CalculatePhi(p,q):
    phi = (p-1)*(q-1)
    return phi

def ChooseE(phi):
    print("Escoja un numero para generar su llave publica")
    e = int(input())
    while math.gcd(e, phi) != 1:
        print("El numero que escogio, debe tener un MCD de 1 con el numero ",phi," Intente de nuevo")
        e = int(input())
        
    return e

def euclide_ext_alg(a, b):
    '''
        as + bt = gcd(a, b)
    '''
    swap = b > a
    if swap :
        t = b 
        b = a
        a = t
        
    table = []
    table.append({'r' : a,
                  'q' : 0,
                  's' : 1,
                  't' : 0})
    q = a // b
    r = a - q * b
    table.append({'r' : b,
                  'q' : q,
                  's' : 0,
                  't' : 1})
    table.append({'r' : r})

    dlast = table[-1]
    while dlast['r'] != 0:
        a = table[-2]['r'] 
        b = dlast['r']
        q  = a // b
        r = a - q * b
        dlast['q'] = q 
        dlast['s'] = table[-3]['s'] - table[-2]['q'] * table[-2]['s']
        dlast['t'] = table[-3]['t'] - table[-2]['q'] * table[-2]['t']
        dlast = {'r' : r}
        table.append(dlast)
        
    if swap: 
        return table[-2]['t'], table[-2]['s']
    return table[-2]['s'], table[-2]['t']

def CalculateD(e,phi):
    d_tuple = euclide_ext_alg(e, phi)
    if d_tuple[0] < 0:
        d = d_tuple[0] + phi
    else:
        d = d_tuple[0]
    return d

def AddZeros(Coded_message_list):
    Message_String = []
    for element in Coded_message_list:
        chain_element = str(element)
        if len(chain_element) == 1:
            chain_element = "0"+chain_element
        Message_String.append(chain_element)
    return Message_String

def CreateBlocks(Message_List,n):
    bloque = ""
    bloques = []
    for element in Message_List:
        bloque = bloque+element
        if len(bloque)>2:
            bloques.append(bloque)
            bloque = ""
    
    return bloques
            
        
    

import math
print("Bienvenido al programa de encriptación de mensaje")
#-----------------------------------------------------------------------------
#Ingresar mensaje y obtener numeros que lo codifiquen
#El mensaje codificado elimina espacios, solo se queda con lo que se encuentra en el abecedario
entry = input("Ingrese el mensaje que se encriptara\n")
Codificacion = ["*","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",0,1,2,3,4,5,6,7,8,9]

Entry = entry.upper()
Mensaje = list(Entry)

Coded_message_list = []

for caracter in Mensaje:
    if caracter in Codificacion:
        Coded_message_list.append(Codificacion.index(caracter))
#------------------------------------------------------------------------------
#Encriptacion del mensaje codificado
#-----------------------------------------------------------------------------
#primer paso: El usuario escoge los primos que lo ayudaran a encriptar su mensaje
print("La encriptacion es de llave publica, por favor siga las instrucciones a continuacion")
p = ChoosePrime()
print("Ha escogido un primo exitosamente, por favor siga las siguientes instrucciones")
q = ChoosePrime()

while IdenticalPrimes(p, q) == True:
    q = ChoosePrime()
    
print("Valor de P:",p)
print("Valor de Q:",q)


#----------------------------------------------------------------------------------
#Se ecoge e, para generar la llave publica y privada
n = p*q
phi = CalculatePhi(p, q)
e = ChooseE(phi)
d = CalculateD(e, phi)

#(n,e) es la llave publica
#(d) es la llave privada

#-----------------------------------------------------------------------------------
#se concatena el mensaje, anteponiendo ceros en los numeros de un digito
Message_List = AddZeros(Coded_message_list)
Blocks = CreateBlocks(Message_List, n)
