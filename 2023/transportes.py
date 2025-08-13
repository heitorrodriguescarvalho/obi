n, m, k = [int(x) for x in input().split()]

prices = {int(index) + 1: int(price) for index, price in enumerate(input().split())}

trips = {}

for _ in range(m):
    v, u, t = [int(x) for x in input().split()]
    
    if v in trips:
        trips[v].append((u, t))
    else:
        trips[v] = [(u, t)]
        
    if u in trips:
        trips[u].append((v, t))
    else:
        trips[u] = [(v, t)]

def verify_trip(current_num, target, current_kind, ignored = [], current_price = 0):    
    if current_num == target:
        return current_price

    current_trips = []
    
    for num, kind in trips[current_num]:
        if num in ignored:
            continue
        
        current_trips.append(verify_trip(
            num,
            target,
            kind,
            [*ignored, current_num],
            current_price + prices[kind] if current_kind != kind else current_price,
        ))
            
    if len(current_trips) == 0:
        return float('inf')
    
    return min(current_trips)

a, b = [int(x) for x in input().split()]

final_price = verify_trip(a, b, 10**5 + 1)

if final_price == float('inf'):
    print(-1)
else:
    print(final_price)