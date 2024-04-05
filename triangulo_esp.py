print("Quantas linhas? ")
linha=int(input())

espaco = linha - 1
print("")
for l in range(1, linha, 1):
  print(" " * espaco, end="")
  print("*" * l)
  espaco -= 1