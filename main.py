'''
Cálculo Numérico - Questão sobre a Regra do Trapézio
Aluna: Raissa Ohana F. O. e Silva
'''
import numpy as np #importando a biblioteca Numpy

def f(x): #definindo a função que será utilizada para resolver esse problema
  return np.cos(x) + x/np.pi

dx = 4*np.pi/3

x = np.linspace(0, 4*np.pi, num=7) #definindo a quantidade de trapézios

y = f(x) 
dx = x[1] - x[0] #espaçamento

I = 0 #iniciando o contador da variável

I += dx*y[0]/2

for i in range(1,x.size-1): 
    I += dx*y[i]

I += dx*y[-1]/2

print(I) #plotando o resultado da taxa de variação