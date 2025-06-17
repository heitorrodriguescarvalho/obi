n = int(input())

parents = [int(i) for i in input().split(" ")]

values = {count + 2: parent for count, parent in enumerate(parents)}

def reorganize(v, current):
    children = [child for child, parent in values.items() if parent == current]
    print(values)
    
    for child in children:
        values[child] = v
        reorganize(v, child)

for _ in range(int(input())):
    operation = [int(i) for i in input().split(" ")]
    
    if operation[0] == 1:
        v, k = operation[1:]
        
        current = v
        for _ in range(k):
            current = values[current]
            
        print(current)
        
    if operation[0] == 2:
        v = operation[1]
        reorganize(v, v)
