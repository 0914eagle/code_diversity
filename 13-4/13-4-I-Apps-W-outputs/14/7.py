
n = int(input())
sizes = [int(x) for x in input().split()]

tower = []
for size in sizes:
    if len(tower) == 0 or tower[-1] < size:
        tower.append(size)
    else:
        while len(tower) > 0 and tower[-1] > size:
            print(tower.pop())
        tower.append(size)

for size in tower:
    print(size)

