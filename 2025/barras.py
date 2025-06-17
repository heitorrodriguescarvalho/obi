n = int(input())
bars = [int(x) for x in input().split()]

max_value = max(bars)

for count in range(max_value):
    result = []
    
    for value in bars:
        if value >= count:
            result.append(1)
        else:
            result.append(0)
            
    print(" ".join([str(x) for x in result]))