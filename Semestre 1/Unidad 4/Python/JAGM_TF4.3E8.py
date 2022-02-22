nombre=str(input("Introduce el nombre de la clase"))
class nombre():
	def __init__ (self,atributo1,atributo2,atributo3,atributo4,atributo5):
		self.atributo1 = atributo1
		self.atributo2 = atributo2
		self.atributo3 = atributo3
		self.atributo4 = atributo4
		self.atributo5 = atributo5
	def getAtributo1(self):
		return self.atributo1
	def getAtributo2(self):
		return self.atributo2
	def getAtributo3(self):
		return self.atributo3
	def getAtributo4(self):
		return self.atributo4
	def getAtributo5(self):
		return self.atributo5

	def imprimirnombre(self):
		print("\nAtributo1:" + self.getAtributo1() + "\nAtributo2:" + self.getAtributo2() + "\nAtributo3:" + self.getAtributo3() + "\nAtributo4:" + self.getAtributo4() +"\nAtributo5:" + self.getAtributo5())
atributo1=input("Favor ingresa el primer atributo")
atributo2=input("Favor ingresa el segundo atributo")
atributo3=input("Favor ingresa el tercer atributo")
atributo4=input("Favor ingresa el cuarto atributo")
atributo5=input("Favor ingresa el quinto atributo")
e = nombre(atributo1,atributo2,atributo3,atributo4,atributo5)
e.imprimirnombre()