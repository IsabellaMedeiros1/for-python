#faça um programa usando laços para desenhar um retangulo na tela com #

for i in range(0, 5):
    print("######")
print("fim do programa")

#faça um programa usando laços para desenhar um retangulo na tela com # solicitando que o usuário informe quantas colunas o retangulo deve ter

print("Quantas linhas você deseja ter: ")
linha = int(input())
print("digite quantas deve ter o retângulo colunas: ")
coluna = int(input())

for i in range(0, linha):
    print("#" * coluna)
print("fim do programa")