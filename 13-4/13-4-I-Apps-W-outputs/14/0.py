
n = int(input())
sizes = list(map(int, input().split()))

tower = []
for i in range(n):
    if sizes[i] not in tower:
        tower.append(sizes[i])
    else:
        index = tower.index(sizes[i])
        tower.insert(index, sizes[i])

print(*tower, sep='\n')

