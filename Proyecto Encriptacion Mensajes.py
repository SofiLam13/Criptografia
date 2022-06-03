# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 12:43:55 2022
Universidad del Valle de Guatemala
Proyecto Criptografía
Pablo Sebastián Herrera 
Sofia Lam Méndez
"""

def mpower(b,n,m):
    if n==0:
        return 1
    else:
        return ((b%m)*(mpower(b, n-1, m)))%m

def DictNumber(m):
    number = ""
    claves={
        "A":"00",
        "B":"01",
        "C":"02",
        "D":"03",
        "E":"04",
        "F":"05",
        "G":"06",
        "H":"07",
        "I":"08",
        "J":"09",
        "K":"10",
        "L":"11",
        "M":"12",
        "N":"13",
        "O":"14",
        "P":"15",
        "Q":"16",
        "R":"17",
        "S":"18",
        "T":"19",
        "U":"20",
        "V":"21",
        "W":"22",
        "X":"23",
        "Y":"24",
        "Z":"25",
        }
    for n in m:
        number=number+claves[n]
    return number

def DictText(n):
    text=""
    lista = [n[y - 2:y] for y in range(2, len(M) + 2, 2)]
    claves=[
        "A","B","C","D","E","F","G","H",
            "I","J","K","L","M","N","O","P",
            "Q","R","S","T","U","V","W","X","Y","Z"]
    for i in lista:
        text=text+claves[int(i)]
    return text

def Crypt(M,p,q,e,N):
    n = p*q
    Mlist = [M[y - 2*N:y] for y in range(N*2, len(M) + N*2, N*2)]
    Mcodificado = []
    for m in Mlist: 
        m=int(m)
        c=str(mpower(m, e, n))
        while len(c)<2*N: c="0"+c
        Mcodificado.append(str(c))
    mensaje = ""
    for m in Mcodificado: 
        mensaje = mensaje+m
    return mensaje
        
def Decrypt(C,p,q,e,N):
    n=p*q
    phi = (p-1)*(q-1)
    d = pow(e, -1, phi)
    Clist = [C[y - 2*N:y] for y in range(N*2, len(C) + N*2, N*2)]
    decodificado = []
    for c in Clist: 
        c=int(c)
        c=str(mpower(c, d, n))
        while len(c)<2*N: c="0"+c
        decodificado.append(str(c))
    mensaje = ""
    for m in decodificado: 
        mensaje = mensaje+m
    return mensaje

    

M = DictNumber("UPLOAD")
print("Su mensaje es: ",M)
print("Su mensaje Encriptado es: ",Crypt(M, 53, 61, 17, 2))
print("---------------------------------------------------")
N = Decrypt("066719470671", 43, 59, 13, 2)
print("Mensaje en código: "+N)
N = DictText(N)
print("Mensaje: "+N)