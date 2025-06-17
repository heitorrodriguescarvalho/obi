n = int(input())
p = int(input())

count = 1
days = 0

while(count <= n):
    days += 1
    count *= p
    
print(days - 1)