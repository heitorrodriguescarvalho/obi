s, t = [int(x) for x in input().split()]

tunnels = {}

for _ in range(t):
    x, y = [int(x) for x in input().split()]
    
    if x in tunnels:
        tunnels[x].append(y)
    else:
        tunnels[x] = [y]

    if y in tunnels:
        tunnels[y].append(x)
    else:
        tunnels[y] = [x]

p = int(input())

def verify_tour(tour):
    for idx in range(len(tour) - 1):
        if not tour[idx] in tunnels[tour[idx + 1]]:
            return False
        
    return True
 
count = 0

for _ in range(p):
    tour = [int(x) for x in input().split()][1:]
    
    if verify_tour(tour): count += 1
    
print(count)  
            