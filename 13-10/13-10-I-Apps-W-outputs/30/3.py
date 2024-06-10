
def count_pictures(r, c, n, k):
    # Initialize a 2D array to represent the orchestra
    orchestra = [[0] * c for _ in range(r)]

    # Fill the orchestra with violinists
    for i in range(r):
        for j in range(c):
            orchestra[i][j] = '*'

    # Place the violists in the orchestra
    for i in range(n):
        x, y = map(int, input().split())
        orchestra[x - 1][y - 1] = '#'

    # Initialize a counter for the number of pictures
    count = 0

    # Iterate over each row in the orchestra
    for i in range(r):
        # Iterate over each column in the orchestra
        for j in range(c):
            # If the current cell is a viola, increment the counter
            if orchestra[i][j] == '#':
                count += 1

    # Return the number of pictures Paul can take
    return count

def main():
    r, c, n, k = map(int, input().split())
    print(count_pictures(r, c, n, k))

if __name__ == '__main__':
    main()

