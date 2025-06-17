n = int(input())
sequence = [int(input()) for _ in range(n)]

max_sequence = 0

for index in range(n):
    count = 0
    current_sequence = []
    
    while index + count < n and not sequence[index + count] in current_sequence:
        current_sequence.append(sequence[index + count])
        count += 1
        
    if (count > max_sequence):
        max_sequence = count
        
print(max_sequence)