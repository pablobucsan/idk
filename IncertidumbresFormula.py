#-*- coding: utf-8 -*-
"""
Created on Thu Apr  8 21:14:36 2021

@author: pablo

"""

import sympy as sym
from math import *
from numpy import *
import Instru

q=input("Quieres ver las instrucciones?   [y/n]   ")

if q=="y":
    Instru.inst()

ind=int(input("Numero de variables independientes, x_i :  "))
medidas=int(input("Numero de medidas de las variables:  "))


xi=[]                     #RECOGE LOS NOMBRES DE LAS VARIABLES
sxi=[]                   #RECOGE LOS NOMBRES DE LAS INCERTIDUMBRES

data=zeros([ind,medidas])
sdata=zeros([ind,medidas])

for i in range(0,ind):               
    x_i=input("Introduce el nombre de las variables:  ")
    x_i=sym.symbols(x_i)
    sx_i=input("Y el nombre de su incertidumbre:   ")
    sx_i=sym.symbols(sx_i)
    xi.append(x_i)
    sxi.append(sx_i)
    
t=False
while t==False:
    print("\n")
    for i in range(0,ind):
        print(i+1,") xi[",i,"]=",xi[i])
    eq=input("\n Teniendo en cuenta la asignacion de variables de arriba introduce la ecuacion f(xi):\n   \n ")
    e=eval(eq)
    print("\n \n f",xi,"=",e)
    l=input("\n \n Es correcta la ecuacion?   [y/n]    ")
    if l=="y":
        t=True
    else:
        t=False



s2=0
for i in range(0,ind):
    s2+=( sym.diff(e,xi[i]) )**2 * sxi[i]**2 
    
print("\n s(f",xi,")^2=",s2)

s2=sym.lambdify([xi,sxi],s2)     #NICE
    


for i in range(0,ind):
    for j in range(0,medidas):
        data[i][j]=float(input(f"Introduce la medida {j+1} de {xi[i]}:    "))
        sdata[i][j]=float(input(f"Introduce la incertidumbre de la medida {j+1} de {xi[i]}:    "))
print("\n ################################################################# \n")       
print(" \n Matriz con las medidas de las distintas variables: \n ", data,"\n \n donde \n ")

for i in range(0,ind):
    print(xi[i],"=",data[i])
    
print(" \n Matriz con las incertidumbres de las distintas medidas: \n ", sdata,"\n \n donde \n ")


for i in range(0,ind):
    print(sxi[i],"=",sdata[i])

e=sym.lambdify([xi],e)

print("\n ################################################################## \n")

for i in range(0,medidas):
    print(i+1,")f",data[: , i:i+1].T,"=",e(data[: , i:i+1]),u"\u00B1", sqrt(s2(data[: , i:i+1],sdata[: , i:i+1])) )

    
    
    

