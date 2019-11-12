import random

#retorna um número inteiro entre 0 e 3
print(random.randrange(4))

#retorna um número inteiro entre 1 e 4 inclusive, internavalo fechado.
print(random.randint(1, 4))

#escolhe aleatoriamente um elemento da lista
lista = [1, 2, 3, 4]
print(random.choice(lista))

#embaralhar um sequência
random.shuffle(lista)
print(lista)

#pegando uma quantidade de elementos aleatórios de uma lista
print(random.sample(lista, 3))
print(random.sample(lista, 2))

#gera um numero em ponto flutuante entre 0 e 1
print(random.random())

#gera um numero em ponto fluante dentre de um intervalo aberto
print(random.uniform(1, 10))

