'''
Ordenação pelo método Selection Sort
'''
 
def selection_sort(lista):
    for i in range(0, len(lista)-1):
        menor = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista
     
while True:
    valor_ini = input("Digite os números do seu vetor, como 10,20,30, digite:")
    valores = list(valor_ini)     
    print (selection_sort(valores))