
def get_input():
    n, m = map(int, input().split())
    mark = [input() for _ in range(n)]
    return n, m, mark

def get_min_nubs(n, m, mark):
    # Initialize a 2D array to store the number of nubs in each cell
    nubs = [[0] * m for _ in range(n)]

    # Loop through each row of the mark and count the number of nubs in each cell
    for i in range(n):
        for j in range(m):
            if mark[i][j] == '#':
                nubs[i][j] += 1

    # Loop through each column of the mark and count the number of nubs in each cell
    for j in range(m):
        for i in range(n):
            if mark[i][j] == '#':
                nubs[i][j] += 1

    # Find the minimum number of nubs in any cell
    min_nubs = min(max(row) for row in nubs)

    return min_nubs

def main():
    n, m, mark = get_input()
    print(get_min_nubs(n, m, mark))

if __name__ == '__main__':
    main()

