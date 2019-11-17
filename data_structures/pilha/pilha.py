#Primeiro elemento a entrar é o último a sair
class Stack: #stack

    def __init__(self):
        self.stack = []
        #numero de elementos da pilha
        self.len_stack = 0

    #insere na pilha
    def push(self, e):
        self.stack.append(e)
        self.len_stack += 1

    
    #remove da pilha
    def pop(self):
        #verifica se a lista está vazia
        if not self.empty():
            self.stack.pop(self.len_stack - 1) 
            self.len_stack -= 1

    #retorna o elemento do top
    def top(self):
        if not self.empty():
            return self.stack[-1]
        return('Pilha vazia')

    #verifica se a lista está vazia
    def empty(self):
        if self.len_stack == 0:
            return True
        return False

    #verifica o tamanho da lista
    def length(self):
        return self.len_stack

s = Stack()

print(s.empty())
print('Tamanho: ', s.length())

#inserindo
s.push(1)
s.push(2)
s.push(3)

print(s.top())
print(s.empty())

#removendo
s.pop()
print(s.top())
print('Tamanho: ',s.length())