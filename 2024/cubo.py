n = int(input())

if (n >= 2):
    f3 = 8
else:
    f3 = 1
    
f2 = max(0, (n - 2) * 12)
f1 = max(0, (n - 2) ** 2 * 6)
f0 = max(0, (n - 2) ** 3)

print(f0)
print(f1)
print(f2)
print(f3)
