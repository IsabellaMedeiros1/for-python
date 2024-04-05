print("Digite quantas linhas você deseja ter: ")
linha = int(input())
print("digite quantas deve ter o retângulo colunas: ")
coluna = int(input())

for l in range(0, linha):
    for c in range(0, coluna):
        print(c + 1, end="")
    print("")
print("fim do programa")