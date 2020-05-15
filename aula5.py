# Diferença da lista para a tupla?
#A lista é mutável e a tupla imutavel

lista = [12, 10, 7, 5]
lista_animal = ['cachorro','gato','elefante','lobo']
lista_animal[0] = 'macaco'
print(lista_animal)

tupla = (1, 10, 12, 14)
tupla[0] = 12
print(len(tupla))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numeraica = list(tupla)
print(type(lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)

#lista.sort()
#lista_animal.sort()
#print(lista)
#print(lista_animal)
#lista_animal.reverse() # Ordena de forma reversa

#lista = [1, 3, 5, 7]
#lista_animal = ['cachorro','gato','elefante']

#nova_lista = lista_animal * 3
#print(nova_lista)


#if 'lobo' in lista_animal
#	print('existe um lobo na lista')
#else:
#	print('não existe um lobo na lista. Será incluido')
#	lista_animal.append('lobo')
#	print(lista_animal)

#lista_animal.remove('elefante')
#print(lista_animal)

#lista_animal.pop() # retira a ultima posição da lista
#print(lista_animal)

#print(lista_animal[1])

#soma= 0
#for x in lista:
#	print(x)
#	soma += x
#print(soma)
#print(max(lista))
#print(min(lista))
#print(min(lista_animal))
#print(max(lista_animal))