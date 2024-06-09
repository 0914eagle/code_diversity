
# Read input
N, M = map(int, input().split())
image_A = [input() for _ in range(N)]
image_B = [input() for _ in range(M)]

# Check if template image B is contained in image A
for i in range(N - M + 1):
    for j in range(N - M + 1):
        match = True
        for k in range(M):
            if image_A[i+k][j:j+M] != image_B[k]:
                match = False
                break
        if match:
            print("Yes")
            exit()

print("No")
