lista = [1, 2, 3, 4]

lista1 = [1, 2, 3]
lista2 = [5, 6, 7, 8, 9, 10]


##concatenação de lista
lista3 = lista1 +  lista2
print(lista3)

#### remover item da lista ###
#elemento da primeira posição
lista.pop(0) 

# elemento da última posicao
lista.pop(len(lista) -1) 

# remove elemento expecifico
lista.remove(3)
print(lista)

### procurando  elemento na lista ###
num = 10

if num in lista:
    print('elemento encontrado')
else:
    print('elemento não encontrado')

### tamanho da lista ###
print(len(lista))


### iterando pelo elementos ###
for i in lista1:
    print(i)

### transformando lista em tupla ###
t_lista = tuple(lista1)
print(type(t_lista))


#### acrescentar elementos ao final da lista ###
lista.append(56)
print(lista)

### inserindo elemento em determinada posicao da lista ###
lista.insert(1, 10)
lista.insert(len(lista), 7)
print(lista)

### ordendando uma lista 
lista.sort()
print(lista)

### imprimindo o ultimo elemento da lista
print(lista[-1])

### imprimindo da posição 1 até 3
print(lista[1:3])

### invertendo a lista
print(lista[::-1])



