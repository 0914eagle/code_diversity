
n = int(input())
sizes = list(map(int, input().split()))

tower = []
for i in range(n):
    if len(tower) == 0 or tower[-1] >= sizes[i]:
        tower.append(sizes[i])
    else:
        print()

