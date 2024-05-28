import sys

cadena = sys.argv[1]
lista = []
for c in cadena:
	lista.append(c)

print(lista)

lista2 = [c for c in cadena]

print(lista2)
