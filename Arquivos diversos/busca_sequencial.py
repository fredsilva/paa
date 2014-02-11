'''
Busca sequencial por Força Bruta
'''
import timeit

def sequencial_search(item, seq_list):
	for i in seq_list:
		if item == i:
			return True		
	return False

'''seq_list = [10,5,1,2,3]
value = int(input('Informe o valor: '))
print(sequencial_search(value, seq_list))'''


#Calcula tempo de execução do código
t = timeit.timeit("sequencial_search(9, list(range(1,10)))", "from __main__ import sequencial_search")
print (t)

