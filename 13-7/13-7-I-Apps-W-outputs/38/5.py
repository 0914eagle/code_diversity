
def solve(H, W, K):
    # Initialize a 2D array to store the amidakuji
    amidakuji = [[0] * (H + 1) for _ in range(W)]

    # Fill in the horizontal lines
    for i in range(W):
        for j in range(1, H + 1):
            amidakuji[i][j] = j

    # Fill in the vertical lines
    for i in range(W):
        for j in range(1, H + 1):
            amidakuji[j][i] = j

    # Count the number of valid amidakuji
    count = 0
    for i in range(W):
        for j in range(1, H + 1):
            if amidakuji[i][j] == K:
                count += 1

    return count % 1000000007

def main():
    H, W, K = map(int, input().split())
    print(solve(H, W, K))

if __name__ == '__main__':
    main()

