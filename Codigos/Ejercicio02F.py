# -*- coding: utf-8 -*-
'funciones del ejercicio 2'

def pal (x) :
    i = 1
    n = x[::-1] #esto voltea la cadena
    if n != x : #y aquí comprueba si ambas son iguales
        i = 0 #el 1 y el 0 son por practicidad, para que fuera más corto
    return i 

def pal_l (x) :
    'Determina si una cadena es palíndromo o no'
    n = pal(x)
    if n == 0 :
        return 'No es palíndromo'
    else :
        return 'Sí es palíndromo'

def error (x) :
    '''Determina el error en una cadena si no
es un palíndromo'''
    n = pal_l (x)
    if n == 'No es palíndromo' :
        return '''Posición %d es diferente a
posición %d''' % (,)
        
    
