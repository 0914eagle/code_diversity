
def solve(N):
    for i in range(N):
        for j in range(N):
            if i != j:
                for k in range(N):
                    if k != i and k != j:
                        if (i, j, k) not in [(0, 0, 0), (0, 0, 40000000), (0, 40000000, 0), (40000000, 0, 0), (40000000, 0, 40000000), (40000000, 40000000, 0), (0, 40000000, 40000000), (40000000, 40000000, 40000000)]:
                            print(i, j, k)
                            return
    print(-1)

