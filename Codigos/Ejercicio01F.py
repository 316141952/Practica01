# -*- coding: utf-8 -*-
'Funciones del ejercicio 1'

def suma_l (x) :
    '''Suma los elementos de una lista'''
    j = 0
    for i in x:
        j = j + i
    print j

    
def orden_l (x) :
    '''Ordena una lista de menor a mayor'''
    for i in range(len(x)-1,0,-1):
        for j in range(i) :
            if x[j]>x[j+1]: 
                t = x[j]
                x[j] = x[j+1]
                x[j+1] = t
    return (x)


def max_l (x) :
    '''Te muestra el elemento máximo
de una lista'''
    orden_l(x)
    n = x.pop()
    return n


def min_l (x) :
    '''Te muestra el elemento mínimo de
una lista'''
    orden_l (x)
    n = x.pop(0)
    return n


def prim_l (x) :
    '''Te dice que números de una lista
son primos'''
    for i in range(len(x)) :
        while x[i]>0 :
            if x[i]==2 or x[i]==3 or x[i]==5 or x[i]==7 :
                return (x[i])
            if x[i]%2==0 or x[i]%3==0 or x[i]%4==0 :
                x[i] = x[i]
            if x[i]%5==0 or x[i]%6==0 or x[i]%7==0 :
                x[i] = x[i]
            if x[i]%8==0 or x[i]%9==0 or x[i]%10==0 :
                x[i] = x[i]
            else :
                return (x[i])
