
n = int(input())
sizes = list(map(int, input().split()))

tower = []
for size in sizes:
    if len(tower) == 0 or tower[-1] < size:
        tower.append(size)
    else:
        tower.insert(0, size)

for size in tower:
    print(size)

