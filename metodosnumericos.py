#importamos las librerias necesarias para las operaciones
import math

#define la tolerancia de errores
def es(n):
  numero = (0.5*10**(2-n));
  return numero;

#función del ejercicio
def f(x):
  #insertamos la función deseada
  resultado = 8*math.sin(x)*math.exp(-x) - 1;
  return resultado;
#hallar el x de f(x)
def derf(x):
  #insertamos la función deseada:
  resultado = (x**2-2.5)/1.8
  return resultado;

#G(X) que la usa el metodo de punto fijo
def g(x):
  #insertamos la función deseada
  resultado = ((x**2-2.5)/1.8)
  return round(resultado, 6)

#Metodo de punto fijo
def fixpt(x0, es, imax=100):
  #inicializar variables
  xr = x0
  ea = 100
  iter = 0

  while(True):
    xrold = xr
    xr = g(xrold)
    iter = iter + 1
    #calcular el EA por cada iteración
    if xr != 0:
      ea = abs((xr - xrold/xr)*100)
      print("iter: ",iter,"XR; ",round(xr,6),"EA: ",round(ea,6)) #mostrar en pantalla el valor de cada iteración
    #si ea es menor a es o si iteraciones alcancza las iteraciones maximas, sale del ciclo
    if ea < es or iter > imax:
      break

  return round(xr,6)# devuelve el calculo verdadero de la raiz aproximada

#Metodo de new Raphson

def newRa(x0, es, imax=100):
  #inicializar variables
  xr = x0;
  iter = 0;
  ea = 100;

  while(True):
    xrold = xr;
    xr = xrold-(f(xrold)/derf(xrold));
    iter = iter +1;

    if xr != 0:
      #calcular el EA por cada iteración
      ea = abs((xr - xrold)/xr)*100;
      print("iter: ",iter,"XR; ",xr,"EA: ",ea);#mostrar en pantalla el valor de cada iteración
    #si ea es menor a es o si iteraciones alcancza las iteraciones maximas, sale del ciclo
    if ea < es or iter > imax:
      break

  return xr;# devuelve el calculo verdadero de la raiz aproximada


#metodo de la secante

def sec(x, x0, es, imax=100):
  #inicializar variables
  xr = x0;
  xr2 = x;
  iter = 0;
  ea = 100;

  while(True):
    xrold = xr;
    xroold = xr2;
    iter = iter + 1
    xr = xrold - (f(xrold)*(xroold-xrold)/(f(xroold)-f(xrold)));#calcular el XR

    xr2 = xrold;
    if xr != 0:
      #calcular el EA por cada iteración
      ea = abs((xr - xrold)/xr)*100;
      print("iter: ",iter,"XR; ",xr,"EA: ",ea);
    #si ea es menor a es o si iteraciones alcancza las iteraciones maximas, sale del ciclo
    if ea < es or iter > imax:
      break

  return xr; # devuelve el calculo verdadero de la raiz aproximada


# metodo de la secante modificada

def secMod(x0, d, es, imax):
  #inicializar variables
  xr = x0;
  iter = 0;
  ea = 100;

  while(True):
    xrold = xr;
    iter = iter + 1
    xr = xrold - (d*xrold*f(xrold)/(f(xrold+d*xrold)-f(xrold)));#calcular el XR
    if xr != 0:
      #calcular el EA por cada iteración
      ea = abs((xr - xrold)/xr)*100;
      print("iter: ",iter,"XR; ",xr,"EA: ",ea);
    #si ea es menor a es o si iteraciones alcancza las iteraciones maximas, sale del ciclo
    if ea < es or iter > imax:
      break

  return xr; # devuelve el calculo verdadero de la raiz aproximada

