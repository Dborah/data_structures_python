def fatorial(n):
    if(n == 0):
        return 1
    return n * fatorial(n -1)

def potencia(base, expoente):
    if(expoente == 0):
        return 1
    return base * potencia(base, expoente - 1)

def area_quadrado(lado):
    return lado * lado