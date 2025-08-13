weights = sorted([int(x) for x in input().split()])

if (sum(weights[0:3]) == sum(weights[3:5]) == weights[5]):
    print("S")
else:
    print("N")