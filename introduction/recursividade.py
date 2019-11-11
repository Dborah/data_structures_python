#### fatorial ###
# 3! = 3  * 2 * 1 = 6
def fatorial(n):
    if(n == 0):
        return 1
    return n * fatorial(n -1)

print(fatorial(3))

#### fibonacci ###
#fibonaci = 1, 1, 2, 3, 5, 8, 13, ...
def fibonacci(n):
    if(n == 1 or n == 2):
        return 1
    return fibonacci(n -1) + fibonacci(n- 2)

print(fibonacci(6))

### potencia ###
'''
    base, expoente
    base = 2
    expoente = 10
    2 ** 10 = 1024
'''
def potencia(base, exp):
    if(exp == 0):
        return 1
    return base * potencia(base, exp - 1)

print(potencia(2,10))
