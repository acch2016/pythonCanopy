# -*- coding: utf-8 -*-
from scipy import * #módulos de optimización, algebra lineal, integración, 
          # interpolación
from numpy import * #manejo de arreglos y operaciones entre ellos
from sympy import * #es para variables simbólicas
from math import * #funciones y operaciones matemáticas
from cmath import * #números complejos y sus funciones
import matplotlib.pyplot as graf   #librería gráfica

#Declaración de Listas
A=[[0,1,2],[3,4,5],[6,7,8]]
print(A)
#Declaración de Tuples
A=[1,2,3],[4,5,6],[7,8,9];print(A)
 # o también A = ([1,2,3],[4,5,6],[7,8,9])
 
#  Equivalente a “linspace de matlab”, genera un ndarray, donde se indica 

# (valor inicial, valor final, número de elementos)
A=linspace(0,6,3)
print(A) #imprime [ 0.  3.  6.]

# Similar a “linspace”, genera un ndarray, donde se indica 
# (valor inicial, valor final (más uno), step)
A=arange(0,7,3)
print(A) #imprime [0 3 6]

################################################################################

# Conversión de una Lista a un Arreglo

A=asarray(A); # o también A = double(A)
print(A) #imprime [0 3 6]

A=[[0,1,2],[3,4,5],[6,7,8]]
A=asarray(A);
print(A) #imprime 
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

A=[[0,1,2],[3,4,5],[6,7,8]]
A = double(A)
print(A) #imprime 
# [[ 0.  1.  2.]
#  [ 3.  4.  5.]
#  [ 6.  7.  8.]]

################################################################################

# Lectura del Tipo de Dato
print(type(A)) # imprime <class 'numpy.ndarray'>

print(type(math.pi)) # imprime <class 'float'>

print(type(double(math.pi))) # imprime <class 'numpy.float64'>

import sys
print(sys.getsizeof(double(3.1416)))  # imprime 32 

################################################################################

# Declarar Lista Vacía
A=[]

################################################################################
################################################################################
################################################################################

# Ejercicios. Formule un Module con el siguiente contenido:
# A. Reproduzca cada uno de los puntos anteriores cambiando el ejemplo numérico.