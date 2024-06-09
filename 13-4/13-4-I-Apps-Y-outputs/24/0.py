
def solve(A, B):
    N = len(A)
    M = len(B)
    grid = [["."]*N for _ in range(M)]

    # Find the first occurrence of the shared letter in A and B
    shared_letter = next((letter for letter in A if letter in B), None)

    # Fill in the grid with the words A and B
    for i in range(N):
        if A[i] == shared_letter:
            for j in range(M):
                if B[j] == shared_letter:
                    grid[j][i] = A[i]
                    break

    for i in range(M):
        for j in range(N):
            print(grid[i][j], end="")
        print()

