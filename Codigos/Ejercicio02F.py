# -*- coding: utf-8 -*-
'funciones del ejercicio 2'

def pal (x) :
    i = 1
    n = x[::-1] #esto voltea la cadena
    if n != x :
        i = 0
    return i 

def pal_l (x) :
    n = pal(x)
    if n == 0 :
        return 'No es palíndromo'
    else :
        return 'Sí es palíndromo'
