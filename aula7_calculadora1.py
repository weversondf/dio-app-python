class Calculadora:
	def __init__(self, num1, num2):
		self.valor_a = num1
		self.valor_b = num2
	def soma(self):
		return self.valor_a + self.valor_b

	def subtracao(self):
		return self.valor_a - self.valor_b

	def multiplicacao(self):
		return self.valor_a * self.valor_b

	def divisao(self):
		return self.valor_a / self.valor_b

calculadora = Calculadora(10, 2)
print(calculadora.valor_a)
print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.divisao())
print(calculadora.multiplicacao())

#def soma(a, b):
#	return a + b

#def subtracao(a, b):
#	return a - b

#def multiplicacao(a, b):
#	return a * b

#def divisao(a, b):
#	return a / b

#print(soma(1, 3))
#print(soma(3, 4))
#print(subtracao(3, 4))