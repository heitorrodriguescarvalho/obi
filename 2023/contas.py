amount = int(input())
a = int(input())
b = int(input())
c = int(input())

bills = sorted([a, b, c])

count = 0

for bill in bills:
    amount -= bill

    if amount < 0:
        print(count)
        exit()

    count += 1
    
print(count)