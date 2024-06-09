
n = int(input())
sizes = list(map(int, input().split()))

tower = []
for i in range(n):
    if len(tower) == 0:
        tower.append(sizes[i])
    else:
        if tower[-1] > sizes[i]:
            tower.append(sizes[i])
        else:
            while tower[-1] <= sizes[i]:
                tower.pop()
            tower.append(sizes[i])

for i in range(n):
    if tower[i] == sizes[i]:
        print(tower[i])
    else:
        print()

