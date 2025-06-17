m, n = [int(x) for x in input().split()]

stock = []

for _ in range(m):
    stock.append([int(x) for x in input().split()])
    
p = int(input())

sells = 0

for _ in range(p):
    kind, size = [int(x) - 1 for x in input().split()]
    
    if (stock[kind][size] > 0):
        stock[kind][size] -= 1
        sells += 1
        
print(sells)