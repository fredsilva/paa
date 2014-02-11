'''
Comparação de Strings por Força Bruta
'''
import timeit

def comp_string(string_new, string_origin):
	for i, c in enumerate(string_origin):
		if string_new[i] != c:
			return False
	return True

def calcula_exec(string):       
    #Calcula tempo de execução do código
    tempo = timeit.timeit("comp_string('{0}', 'Fred')".format(string), "from __main__ import comp_string")
    return tempo