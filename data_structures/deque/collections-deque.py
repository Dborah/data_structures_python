from collections import deque

d = deque()

d.append(1)     # adiciona do lado direito
d.appendleft(2) #adiociona do lado esquerdo
d.append(3)
d.appendleft(4)

# 4 2 1 3 

for i in d:
    print(i, end=' ')

print("")

d.pop()      # remove do lado direto
d.popleft()  #remove da esqueda
for i in d:
    print(i, end=' ')

print("")

d.remove(1) #remove um elemento especifico
for i in d:
    print(i, end=' ')