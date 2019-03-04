# -*- coding: utf-8 -*-
import random
from random import randint
'funciones del ejercicio 3'

def dados (x) :
    '''Te dice la frecuencia de una
cierta cara del dado'''
    n = 0
    m = 0
    L = range (10000)
    for i in L :
        i = randint(1,100)
        if i == x :
            n = n + 1
            m = m + n
    return m 

def tablita (x) :
    '''Da una tabla con la cara y la frecuencia'''
    m = dados (x)
    print 'Cara     Frecuencia'
    print '%g          %g' % (x,m)

