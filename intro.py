# -*- coding: utf-8 -*-

# from scipy import * #módulos de optimización, algebra lineal, integración, 
          #interpolación
# from numpy import * #manejo de arreglos y operaciones entre ellos
from sympy import * #es para variables simbólicas
# from math import * #funciones y operaciones matemáticas
# from cmath import * #números complejos y sus funciones
# import matplotlib.pyplot as graf   #librería gráfica
#from tkinter import *


def f(t):
    y = pow(t,3) + 4*pow(t,2) - 10
    return y
t=1
z=f(t) 

def cls():
    print('\n' *50)
   
    #comentario
    
def hola():
    print('hola\n' *5)

i=4;j=7
if i > j:
    print ('mayor')
elif i < j:
    print ('menor')
else:
    print ('igual')
    
for i in range(2,4):
    for j in range(1,4):
        print ('%d * %d = %d' % (i,j,i*j))
        
# op = double(3.1416)
# print('%e' %op)
op2 = 3.1416
print('%f' %op2)
#op3 = DoubleVar (3.1416)

#TODO

import sys
# size = sys.getsizeof(op)
size2 = sys.getsizeof(op2)
#size3 = sys.getsizeof(op3)
# print(size)
print(size2)
#print(size3)

# sys.displayhook = pprint
x=Symbol('x');print(x)
f=cos(x)-x; print(f)

df= diff(f,x,1);print(df)
sf = integrate(f,x);print(sf)
sfab = integrate(f,(x,0,pi));print(sfab)