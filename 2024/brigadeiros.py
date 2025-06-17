n, k, t = [int(i) for i in input().split(" ")]

candy = [int(i) for i in input().split(" ")]
group = [idx for idx, val in enumerate(input().split(" ")) if val == "1"]

candy_by_person = []

for idx, person in enumerate(group):
    for i in range(person - t, person + t + 1):
        if i < 0 or i >= n:
            continue
        
        try:
            candy_by_person[idx][candy[i]] = i
        except:
            candy_by_person.append({ candy[i]: i })
            
            
n = len(candy_by_person)
used_indices = set()
max_sum = -1
best_path = []

def backtrack(i, current_sum, path):
    global max_sum, best_path
    if i == n:
        if current_sum > max_sum:
            max_sum = current_sum
            best_path = path[:]
        return

    for k, v in candy_by_person[i].items():
        if v not in used_indices:
            used_indices.add(v)
            path.append((k, v))
            backtrack(i + 1, current_sum + k, path)
            path.pop()
            used_indices.remove(v)

backtrack(0, 0, [])

print(max_sum)