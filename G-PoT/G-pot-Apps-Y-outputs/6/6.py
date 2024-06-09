
b, d, c, l = map(int, input().split())

possible_solutions = []
for i in range(b + 1):
    for j in range(d + 1):
        k = l - 2*i - 4*j
        if k >= 0 and k <= c:
            possible_solutions.append((i, j, k))

if len(possible_solutions) == 0:
    print("impossible")
else:
    for solution in sorted(possible_solutions):
        print(*solution)
