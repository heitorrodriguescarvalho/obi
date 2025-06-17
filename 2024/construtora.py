input()

builds = [int(i) for i in input().split(" ")]
builds_count = len(builds)
max_height = max(builds)

phases_count = 0

while(builds.count(max_height) != builds_count):
    phases_count += 1
        
    min_height_value = max_height
    min_height_index: int
    
    for index, height in enumerate(builds):
        if height < min_height_value:
            min_height_value = height
            min_height_index = index
            
    count = 1
    
    while min_height_index + count < len(builds) and builds[min_height_index + count] == min_height_value:
        count += 1
        
    for index in range(min_height_index, min_height_index + count):
        builds[index] += 1
        
print(phases_count)
