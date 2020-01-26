# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

from scipy import * #módulos de optimización, algebra lineal, integración,
      	#interpolación
from numpy import * #manejo de arreglos y operaciones entre ellos
from sympy import * #es para variables simbólicas
from math import *
#funciones y operaciones matemáticas
from cmath import * #números complejos y sus funciones
import matplotlib.pyplot as graf   #librería gráfica



def f(x):
	y = pow(x,3) + 4*pow(x,2) - 10
	return y
def cls():
	print('\n' *50)
    
	#comentario
    
def hola():
	print('hola\n' *5)

x=4;y=7
if x > y:
	print ('mayor')
elif x < y:
	print ('menor')
else:
	print ('igual')
    
for x in range(2,4):
	for y in range(1,4):
    	print ('%d * %d = %d' % (x,y,x*y))
   	 
op = double(3.1416)
print('%f' %op)
op

#TODO investigar sizeOf en Python

import sys
x = 2
size = sys.getsizeof(op)

print(size)

# DoubleVar (float)

