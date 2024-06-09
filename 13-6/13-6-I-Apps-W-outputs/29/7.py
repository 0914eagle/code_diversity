
def get_wrongness_sum(N, C, D, c):
    # Initialize a 2D array to store the wrongness of each square
    wrongness = [[0] * N for _ in range(N)]

    # Loop through each square and calculate its wrongness
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            wrongness[i][j] = D[c[i][j] - 1][c[i][j] - 1]
            for k in range(N):
                if k == j:
                    continue
                if (i + j) % 3 == (k + j) % 3:
                    wrongness[i][j] += D[c[i][j] - 1][c[k][j] - 1]
                else:
                    wrongness[i][j] += D[c[i][j] - 1][c[k][j] - 1]

    # Return the minimum possible sum of wrongness of all squares
    return min(sum(row) for row in wrongness)

def main():
    N, C = map(int, input().split())
    D = []
    for _ in range(C):
        D.append(list(map(int, input().split())))
    c = []
    for _ in range(N):
        c.append(list(map(int, input().split())))
    print(get_wrongness_sum(N, C, D, c))

if __name__ == '__main__':
    main()

