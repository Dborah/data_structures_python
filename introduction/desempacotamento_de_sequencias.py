### desempacotando lista ###
lista = [ 1, 2, 3, 4]

a, _, _, b = lista

print(a)
print(b)

### desempacotando tupla ###

tupla = (1, 2, 3)

a, b, c = tupla

print(a)
print(b)
print(c)

### desempacotando string ###
nome = "abc"

c1, c2, _ = nome

print(c1)
print(c2)

### retornando mais de um valor na funcao ###
def func(x, y):
    return x**2, y**2

print(func(2, 3))

### desempacotando resultada da função ###
r1, r2 = func(2, 3)
print(r1)
print(r2)

### parametro opcional ###
def func(x, y = 3):
    return x**2, y**2

print(func(2))
