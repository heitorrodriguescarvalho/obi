lines_count, x_start, x_end = [int(i) for i in input().split(" ")]

lines = []
for _ in range(lines_count):
    a, b = input().split(" ")
    lines.append({"a": int(a), "b": int(b)})

points_count = 0

for idx, line1 in enumerate(lines):
    for line2 in lines[idx + 1:]:        
        if line1["a"] == line2["a"]:
            continue
        
        point = (line1["b"] - line2["b"]) / (line2["a"] - line1["a"])
                
        if (point >= x_start and point <= x_end):
            points_count += 1
        
print(points_count)
