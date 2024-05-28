import random

class Clase:
	def __init__(self, clase):
		self.clase = clase
		self.numero = random.randint(1,100)

	def say_hello(self):
		print(f'Hola, {self.clase, self.numero}')



clase = Clase('Pendejo')
clase.say_hello()

