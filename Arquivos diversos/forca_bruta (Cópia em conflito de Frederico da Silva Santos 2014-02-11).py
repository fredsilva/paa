'''
Força Bruta
Projeto e Análise de Algoritmos
UFT - Universidade Federal do Tocantins
'''

import random
from time import time
from math import sqrt

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

	#return lista


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

	#return lista


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
		if texto[i] != caracter:
			tempo_exe = time() - inicio
			print('Tempo de execução: %f s' % tempo_exe)
			return False
	
	tempo_exe = time() - inicio
	print('Tempo de execução: %f s' % tempo_exe)
	return True	


def par_proximo(lista):
	'''
	Retorna os pares mais próximos dado um conjunto de pontos
	'''
	inicio = time()
	dmin = 1000 # Maior valor entre os pontos
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
	random.shuffle(lista)
	return lista