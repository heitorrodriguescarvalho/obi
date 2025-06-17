input()

string = input()

count = []

index = 0

while index < len(string):
    
    if len(count) == 0 or count[-1][0] != string[index]:
        count.append([string[index], 1])
    else:    
        count[-1][1] += 1
        
    index += 1
    
print(" ".join(f"{x[1]} {x[0]}" for x in count))