#FIFO = o primeiro elemento a entrar é o primeiro a sair 
#Insere no final e remove do início

class Queue:

    def __init__(self):
        self.queue = []
        self.len_queue = 0;

    def push(self, e):
        self.queue.append(e)
        self.len_queue += 1

    def pop(self):
        if not self.empty():
            self.queue.pop(0)
            self.len_queue -= 1

    def empty(self):
        if self.len_queue == 0:
            return True
        return False

    def length(self):
        return self.len_queue

    #primeiro elemento da fila
    def front(self):
        if not self.empty():
            return self.queue[0]
        return None

q = Queue()
q.push(1)
q.push(2)
q.push(3)
print(q.front())
q.pop()
q.pop()
q.pop()
print(q.front())