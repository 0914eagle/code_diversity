
def minimal_inspections(N, M, names_list, initial_order):
    inspections = []
    name_count = {}
    for name in names_list:
        if name not in name_count:
            name_count[name] = 1
        else:
            name_count[name] += 1
    
    for name in initial_order:
        if name in name_count and name_count[name] > 0:
            name_count[name] -= 1
        else:
            inspections.append(name)
    
    return len(inspections), inspections

# Read input
N, M = map(int, input().split())
names_list = list(map(int, input().split()))
initial_order = list(map(int, input().split()))

# Call the function and print output
min_inspections, new_positions = minimal_inspections(N, M, names_list, initial_order)
print(min_inspections)
print(*new_positions)
