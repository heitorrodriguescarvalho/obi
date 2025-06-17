h = int(input())
m = int(input())
s = int(input())
t = int(input())

s += t
m += s // 60
s %= 60
h += m // 60
m %= 60
h %= 24

print(h)
print(m)
print(s)