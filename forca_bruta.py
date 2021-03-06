'''
Força Bruta
Projeto e Análise de Algoritmos
UFT - Universidade Federal do Tocantins
Autor: Frederico da Silva Santos
'''

from random import randint, shuffle, choice
import string

def bubble_sort(lista):
	'''
	Realiza a ordenação de uma lista com o método Bubble Sort
	'''		

	for i in range(0, len(lista)-1):
		for j in range(0, len(lista)-1-i):
			if lista[j] > lista[j+1]:
				lista[j], lista[j+1] = lista[j+1], lista[j]	
	return lista


def selection_sort(lista):
	'''
	Realiza a ordenação de uma lista com o método Selection Sort
	'''
	for i in range(0, len(lista)-1):
		menor = i
		for j in range(i + 1, len(lista)):
			if lista[j] < lista[menor]:
				menor = j
		lista[i], lista[menor] = lista[menor], lista[i]
	return lista


def busca_sequencial(item, lista):
	'''
	Realiza uma busca sequencial em uma lista
	'''
	for i, v in enumerate(lista):
		if item == v:		
			return i	
	return False


def compara_strings(texto, amostra):
	'''
	Comparação de strings por força bruta
	'''		
	for i, caracter in enumerate(amostra):
		if texto[0] == caracter:			
			if sub_string(texto, amostra[i:len(texto)]):
				return True
	return False			


def sub_string(texto, sub_amostra):
	'''
	Comparação de substrings dentro de uma string
	'''	
	for i, caracter in enumerate(sub_amostra):
		if texto[i] != caracter:			
			return False		
	return True


def par_proximo(lista):
	'''
	Retorna os pares mais próximos dado um conjunto de pontos
	'''	
	dmin = 1000000 
	for i in range(0, len(lista)-1):		
		for j in range(i + 1, len(lista)):
			dif = (lista[i][0] - lista[j][0])**2 + (lista[i][1] - lista[j][1])**2			
		if dif < dmin:
			dmin = dif
			index1 = i;
			index2 = j;		
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
