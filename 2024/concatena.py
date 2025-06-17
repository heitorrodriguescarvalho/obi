n, q = [int(i) for i in input().split(" ")]
nums = input().split(" ")
lists = []

for _ in range(q):
    current_list = [int(i) for i in input().split(" ")]
    lists.append((current_list[0] - 1, current_list[1] - 1))

sums = []

for start, end in lists:
    current_sum = 0
    current_list = nums[start:end + 1]
    
    for i1, n1 in enumerate(current_list):
        for i2, n2 in enumerate(current_list):
            if (i1 == i2):
                continue
            
            current_sum += int(n1 + n2)
                    
    sums.append(current_sum)

for num in sums:
    print(num)        