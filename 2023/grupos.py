e, m, d = [int(x) for x in input().split()]

together = []
separated = []

for _ in range(m):
    together.append([int(x) for x in input().split()])
    
for _ in range(d):
    separated.append([int(x) for x in input().split()])
    
groups = []

for _ in range(e // 3):
    groups.append([int(x) for x in input().split()])

count = 0

for x, y in together:
    satisfied = False
    
    for group in groups:
        if x in group and y in group:
            satisfied = True
            break
        
    if not satisfied:
        count += 1
        
for x, y in separated:
    satisfied = True
        
    for group in groups:
        if (x in group) and (y in group):
            satisfied = False
            break
          
    if not satisfied:
        count += 1
        
print(count)
