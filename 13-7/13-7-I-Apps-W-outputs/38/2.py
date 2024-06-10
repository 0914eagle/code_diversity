
def amidakuji(H, W, K):
    # Initialize a 2D array to store the amidakuji
    amidakuji = [[0] * (H + 1) for _ in range(W)]

    # Fill in the vertical lines
    for i in range(W):
        amidakuji[i][0] = 1
        amidakuji[i][H] = H + 1

    # Fill in the horizontal lines
    for i in range(W):
        for j in range(1, H):
            amidakuji[i][j] = j + 1

    # Count the number of valid amidakuji
    count = 0
    for i in range(W):
        for j in range(1, H):
            if amidakuji[i][j] == K:
                count += 1

    return count % 1000000

def main():
    H, W, K = map(int, input().split())
    print(amidakuji(H, W, K))

if __name__ == '__main__':
    main()

