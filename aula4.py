# Exemplo while
a = int(input('Primeiro bimestre: '))
while a > 10:
	a = int(input('Você digitou errado. Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
while b > 10:
	b = int(input('Você digitou errado. Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
while c > 10:
	c = int(input('Você digitou errado. Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
while d > 10:
	d = int(input('Você digitou errado. Quarto bimestre: '))
media = (a + b + c + d) / 4
if a <= 10 and b <= 10 and c <= 10 and d <=10:
	print('media: {}'.format(media))
else:
	print('foi informado alguma nota errada')





#nota = int(input('Entre com a nota: '))
#while nota > 10:
#	nota = int(input('Nota inválida. Entre com a nota correta: '))
#print(nota)


#a = 0
#while a <= 10:
#	print(a)
#	a += 1



# Exemplo for
#a = int(input('Entre com um valor: '))
#for num in range(a+1):
# #for num in range(101):
#	div = 0
#	for x in range (1, num+1):
#		resto = num % x
#		#print(num, resto)
#		if resto == 0:
#			#div = div + 1
#			div += 1

#	if div == 2:
#		print(num)
# Resultado
#2
#3
#5
#7
#11
#13
#17
#19
#23
#29
#31
#37
#41
#43
#47
#53
#59
#61
#67
#71
#73
#79
#83
#89
#97

#a = int(input('Entre como número: '))

#div = 0
#for x in range (1, a+1):
#	resto = a % x
#	print(a, resto)
#	if resto == 0:
#		#div = div + 1
#		div += 1

#if div == 2:
#	print('número {} é primo'.format(a))
#else:
#	print('numero {} não é primo',format(a))
