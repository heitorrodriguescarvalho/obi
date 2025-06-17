n, m = [int(i) for i in input().split(" ")]

values = []

for _ in range(n):
    values.append([int(i) for i in input().split(" ")])
    
def try_around(total, powers, used):
    current_sum = 0
    
    new_powers = powers.copy()
                  
    for key, val in powers.items():
        if key in used:
            continue
        
        if total >= val:
            current_sum += val
            
            used.append(key)
            
            x, y = key
            
            if (y + 1 < n):
                new_powers[(x, y + 1)] = values[y + 1][x] 
            if (y - 1 >= 0):
                new_powers[(x, y - 1)] = values[y - 1][x] 
            if (x + 1 < m):
                new_powers[(x + 1, y)] = values[y][x + 1] 
            if (x - 1 >= 0):
                new_powers[(x - 1, y)] = values[y][x - 1] 
            
    if (current_sum != 0):
        return try_around(total + current_sum, new_powers, used)
    
    return total
    

for y in range(n):
    results = []
    
    for x in range(m):
        powers = {}
        total = values[y][x]
        
        if (y + 1 < n):
            powers[(x, y + 1)] = values[y + 1][x] 
        if (y - 1 >= 0):
            powers[(x, y - 1)] = values[y - 1][x] 
        if (x + 1 < m):
            powers[(x + 1, y)] = values[y][x + 1] 
        if (x - 1 >= 0):
            powers[(x - 1, y)] = values[y][x - 1] 
                
        results.append(str(try_around(total, powers, [(x, y)])))
        
    print(" ".join(results))