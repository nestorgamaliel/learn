def getint():
	try:
		valor = input("Ingrese un entero ")
		entero = int(valor)
		print(f'Su numero es {entero}')
	except(ValueError):
		print("No es un entero, intentelo de nuevo")
		getint()
		
	
getint()
