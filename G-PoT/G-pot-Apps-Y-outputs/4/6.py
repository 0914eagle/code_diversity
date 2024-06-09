
# Read input
N, M = map(int, input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]

# Check if template image B is contained in image A
for i in range(N - M + 1):
    for j in range(N - M + 1):
        match = True
        for k in range(M):
            for l in range(M):
                if A[i + k][j + l] != B[k][l]:
                    match = False
                    break
            if not match:
                break
        if match:
            print("Yes")
            exit()

print("No")