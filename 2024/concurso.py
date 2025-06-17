n, k = input().split(" ")
notas = input().split(" ")

notas = [int(nota) for nota in notas]
notas.sort()
notas.reverse()

corte = notas[int(k) - 1]

print(corte)