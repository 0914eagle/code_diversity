
N, M = map(int, input().split())
names_list = list(map(int, input().split()))
initial_order = list(map(int, input().split()))

positions = {}
for i in range(N):
    positions[initial_order[i]] = i

inspections = []
for name in names_list:
    if positions[name] == 0:
        inspections.append(positions[name] + 1)
    else:
        inspections.append(positions[name])
    
    new_position = positions[name]
    for key, value in positions.items():
        if value < new_position:
            positions[key] += 1
    positions[name] = 0

print(len(inspections))
print(" ".join(map(str, inspections)))
