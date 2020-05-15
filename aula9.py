def escrever_arquivo(texto):
	diretorio = 'd:/Weverson-64GB/Cursos/Global Fullstack Developer - Digital Innovation One/18 Introdução à programação com Python/app_python/teste.txt'
	arquivo = open(diretorio, 'w')
	arquivo.write(texto)
	arquivo.close()

def atualizar_arquivo(texto):
	diretorio = 'd:/Weverson-64GB/Cursos/Global Fullstack Developer - Digital Innovation One/18 Introdução à programação com Python/app_python/teste.txt'
	arquivo = open(diretorio, 'a')
	arquivo.write(texto)
	arquivo.close()

def ler_arquivo(nome_arquivo):
	diretorio = 'd:/Weverson-64GB/Cursos/Global Fullstack Developer - Digital Innovation One/18 Introdução à programação com Python/app_python/teste.txt'
	arquivo = open(diretorio, 'r')
	texto = arquivo.read()
	print(texto)

def media_notas(nome_arquivo):
	arquivo = open(nome_arquivo, 'r')
	aluno_nota = arquivo.read()
	#print(aluno_nota)
	lista_media = []
	aluno_nota = aluno_nota.split('\n')
	#print(aluno_nota)
	for x in aluno_nota:
		lista_notas = x.split(',')
		aluno = lista_notas[0]
		lista_notas.pop(0)
		print(aluno)
		print(lista_notas)
		media = lambda notas: sum([int(i) for i in notas]) / 4
		lista_media.append({aluno:media(lista_notas)})
	return lista_media
		#print(media(lista_notas))

def copia_arquivo(nome_arquivo):
	import shutil
	#shutil.copy(nome_arquivo, 'C:/Projetos/globallabs/notas_alunos.txt')
	shutil.copy(nome_arquivo, 'd:/Weverson-64GB/Cursos/Global Fullstack Developer - Digital Innovation One/18 Introdução à programação com Python/app_python/notas_alunos.txt')

def move_arquivo(nome_arquivo):
	shutil.move(nome_arquivo, 'C:/Projetos/globallabs/')

if __name__ == '__main__':
	move_arquivo('notas.txt')
	#copia_arquivo('d:/Weverson-64GB/Cursos/Global Fullstack Developer - Digital Innovation One/18 Introdução à programação com Python/app_python/notas.txt')
	#lista_media = media_notas('d:/Weverson-64GB/Cursos/Global Fullstack Developer - Digital Innovation One/18 Introdução à programação com Python/app_python/notas.txt')
	#print(lista_media)

	#escrever_arquivo('Primeira linha.\n')
	#atualizar_arquivo('Segunda linha.\n')
	#atualizar_arquivo('Terceira linha.\n')
	#ler_arquivo('teste.txt')