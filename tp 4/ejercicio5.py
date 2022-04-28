"""Ejercicio 5: Escribir un algoritmo que lea números enteros hasta que se ingrese un 0,
y muestre el máximo, el mínimo (sin considerar el 0) y la media (promedio) de todos ellos.
Piense cómo debe inicializar las variables."""
actual=int(input("Ingrese un numero: "))
maximo=actual
minimo=actual
i=1
promedio=actual
while actual!=0:
    i+=1
    actual=int(input ("Ingrese un numero: "))
    promedio+=actual
    if minimo>actual and actual !=0:
        minimo=actual
    if maximo<actual:
        maximo=actual
promedio/=i
print ("El promedio es: ", promedio, "\n")
print ("El maximo es: ", maximo, "\n")
print ("El minimo es: ", minimo )