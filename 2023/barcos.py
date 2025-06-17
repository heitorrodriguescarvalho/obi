n, b = [int(x) for x in input().split()]

trips = {}

for _ in range(b):
    i, j, p = [int(x) for x in input().split()]
    
    if i in trips:
        trips[i].append((j, p))
    else:
        trips[i] = [(j, p)]
        
    if j in trips:
        trips[j].append((i, p))
    else:
        trips[j] = [(i, p)]
        
c = int(input())

def verify_trip(current_num, target, ignored = [], current_people = 10**5):
    if current_num == target:
        return current_people
    
    current_trips = []
    
    for num, max_people in trips[current_num]:
        if num in ignored:
            continue
        
        current_trips.append(verify_trip(num, target, [*ignored, current_num], min(current_people, max_people)))
        
    if len(current_trips) == 0:
        return 0
    
    return max(current_trips)

for _ in range(c):
    x, y = [int(x) for x in input().split()]
    
    print(verify_trip(x, y))
    