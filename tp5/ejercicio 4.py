"""Ejercicio 4: Una empresa factura a sus clientes el último día de cada mes. 
Si el cliente paga su factura dentro de los primeros 10 días del mes siguiente, 
tiene un descuento de $120 o del 2% de la factura, lo que resulte más conveniente 
para el cliente. Si paga en los siguientes 10 días del mes deberá pagar el importe 
original de la factura, mientras que si paga después del día 20 deberá abonar una 
multa de $150 o del 10% de su factura, lo que resulte mayor. 
Escriba un algoritmo que lea el número del cliente y el total de la factura, 
y emita un informe donde conste el número del cliente y los tres importes que podrá 
abonar según la fecha de pago."""

def calcular_pago(cliente, factura):
    print("\nSi el cliente",cliente,"paga:")
    if(factura*.98<factura-120):
        print("Antes hasta el 10, debe: $","{:.2f}".format(factura*.98))
    else:
        print("Antes hasta el 10, debe: $",factura-120);
    print("Luego del 10 y hasta el 20, debe: $", "{:.2f}".format(factura))
    if(factura*1.1<factura+150):
        print("Luego del 20, debe: $",factura+150)
    else:
        print("Luego del 20, debe: $","{:.2f}".format(factura*1.1))
calcular_pago(input("ingrese cliente: "),float(input("ingrese monto: ")))