#########   lambda  #########
def potencia(x):
     return x ** 2

potencia_lambda  =  lambda x: x ** 2

#print(potencia(4))
#print(potencia_lambda(4))

def fatorial(n):
    if(n == 0):
        return 1
    return (n * fatorial(n - 1))

fatorial_lambda =  lambda n: n *  fatorial_lambda(n -1) if n > 1 else 1

#print(fatorial(5))
#print(fatorial_lambda(5))


#########   map  #########
#aplica uma funcão em todos os elementos de uma ou mais sequẽncias
lista = [1, 2, 3]
m =  map(lambda x: x ** 2, lista)
for i in m:
    print(i)


#########   reduce  #########
#aplica uma função sobre uma sequência e acumula do valor de retorno apartir de uma valor inicial
import functools
print(functools.reduce(lambda x,y: x+y,[1,2,3,4]))

#########   filter  #########
#filtra elementos que correspondem a determinada condição
f = filter(lambda x: x%2 == 0, range(10))
for i in f:
    print(i)



