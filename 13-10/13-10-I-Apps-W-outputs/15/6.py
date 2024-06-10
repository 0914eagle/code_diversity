
def get_crosses(matrix):
    n = len(matrix)
    m = len(matrix[0])
    crosses = 0
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if matrix[i][j] == 'X' and matrix[i - 1][j - 1] == 'X' and matrix[i - 1][j + 1] == 'X' and matrix[i + 1][j - 1] == 'X' and matrix[i + 1][j + 1] == 'X':
                crosses += 1
    return crosses

def main():
    n = int(input())
    matrix = [input() for _ in range(n)]
    print(get_crosses(matrix))

if __name__ == '__main__':
    main()

