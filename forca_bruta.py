'''
Força Bruta
Projeto e Análise de Algoritmos
UFT - Universidade Federal do Tocantins
'''

from random import randint, shuffle, choice
from time import time
import string

def bubble_sort(lista):
	'''
	Realiza a ordenação de uma lista com o método Bubble Sort
	'''	
	inicio = time()

	for i in range(0, len(lista)-1):
		for j in range(0, len(lista)-1-i):
			if lista[j] > lista[j+1]:
				lista[j], lista[j+1] = lista[j+1], lista[j]		

	tempo_exe = time() - inicio
	print('Tempo de execução: %f s' % tempo_exe)

	return lista


def selection_sort(lista):
	'''
	Realiza a ordenação de uma lista com o método Selection Sort
	'''
	inicio = time()

	for i in range(0, len(lista)-1):
		menor = i
		for j in range(i + 1, len(lista)):
			if lista[j] < lista[menor]:
				menor = j
		lista[i], lista[menor] = lista[menor], lista[i]

	tempo_exe = time() - inicio
	print('Tempo de execução: %f s' % tempo_exe)

	return lista


def busca_sequencial(item, lista):
	'''
	Realiza uma busca sequencial em uma lista
	'''
	inicio = time()
	
	for i, v in enumerate(lista):
		if item == v:
			
			tempo_exe = time() - inicio			
			print('Tempo de execução: %f s' % tempo_exe)

			return i	
	
	tempo_exe = time() - inicio
	print('Tempo de execução: %f s' % tempo_exe)

	return False

def compara_strings(texto, amostra):
	'''
	Comparação de strings por força bruta
	'''
	inicio = time()
	
	for i, caracter in enumerate(amostra):
		if texto[0] == caracter:			
			if sub_string(texto, amostra[i:len(texto)]):
				
				tempo_exe = time() - inicio
				print('Tempo de execução: %f s' % tempo_exe)
				
				return True
	
	tempo_exe = time() - inicio
	print('Tempo de execução: %f s' % tempo_exe)				
	
	return False			

def sub_string(texto, sub_amostra):
	'''
	Comparação de substrings dentro de uma string
	'''	
	for i, caracter in enumerate(sub_amostra):
		if texto[i] != caracter:
			tempo_exe = time() - inicio			
			return False		
	return True


def par_proximo(lista):
	'''
	Retorna os pares mais próximos dado um conjunto de pontos
	'''
	inicio = time()
	dmin = 1000000 
	for i in range(0, len(lista)-1):		
		for j in range(i + 1, len(lista)):
			dif = (lista[i][0] - lista[j][0])**2 + (lista[i][1] - lista[j][1])**2			
		if dif < dmin:
			dmin = dif
			index1 = i;
			index2 = j;	
	tempo_exe = time() - inicio
	print('Tempo de execução: %f s' % tempo_exe)
	return (index1,index2)


def gera_lista(n):
	'''
	Gera uma lista desordenada com um tamanho N
	'''
	lista = list(range(1,int(n+1)))
	shuffle(lista)
	return lista

def gera_pontos(n):
	'''
	Gera uma lista de pontos com tamanho N
	'''
	pontos = []
	while len(pontos) < n:
		pontos.append((randint(0,100), randint(0,100)))
	return pontos

def gera_string(n):
	'''
	Gera uma string com N caracteres
	'''
	caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits
	string_gerada = ''
	for x in range(n):
		string_gerada += ''.join(choice(caracteres))
	return string_gerada
