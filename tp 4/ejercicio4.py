posicion=0
actual=0
mayor=-1
suma=0
'''print("ingrese cantidad de numeros: ")
cantidad_de_numeros=int(input())'''

for i in range(1,11):
    print("ingrese un numero: ")
    actual=int(input())
    suma+=actual
    if (i==0):
        posicion=1
        mayor=actual
    else:
        if(mayor<actual):
            posicion=i
            mayor=actual
print("Mayor: ", mayor,"\nposicion: ", posicion, "\npromedio: ", suma/10)