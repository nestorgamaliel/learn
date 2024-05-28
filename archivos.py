f = open("temps.dat", "a")
lista = ['Hola', 'Mundo']

for l in lista:
	f.write(l + '\t')

f.close()


f = open("temps.dat", "r")
for l in f:
	print(l.split())
