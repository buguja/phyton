lista= [1991, "texto", True, ["contenido", 2012]]
print lista
#imprime la lista.

print lista[1]
#imprime un elemento de la lista.

print lista[3][0]
#imprime un elemento de una sublista.

lista[1]= 12
#cambia el valor de un elemento de la lista.

nuevaLista= lista[0 : 3]
#copia los elementos de una lista [inicio : fin : saltos] 
#si quiero saltos de uno en uno "saltos" debería ser 2
#si quiero saltos de dos en dos "saltos" debería ser 3
#siempre es saltos mas 1

lista[0 : 2]= ["posicion 0", "posicion 1"]
#reemplazar un grupo de la lista.

listaInversa= lista[-1] #lista[-3]
#dentro del corchete debe ir la posicion que se quiere imprimir,
#cuenta de derecha a izquierda y no hay -0