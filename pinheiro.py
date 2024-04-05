print('quantas linhas o pinheiro deve ter? ')
linhas = int(input())

j = 0

space = linhas
for l in range(1, linhas + 1):

    print(' ' * space, end="")
    print('*' * (l + j))
    space -= 1
    j += 1

if linhas <= 10:
    print(' ' * (linhas-1) + "|  |") 

elif linhas > 10 and linhas <= 30:
    for l in range(4):
        print(' ' * (linhas-3) + "|     |") 


else:
    for l in range(7):
        print(' ' * (linhas-6) + "|         |") 