
def get_input():
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(input())
    return matrix

def get_crosses(matrix):
    crosses = 0
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            if matrix[i][j] == 'X' and matrix[i - 1][j - 1] == 'X' and matrix[i - 1][j + 1] == 'X' and matrix[i + 1][j - 1] == 'X' and matrix[i + 1][j + 1] == 'X':
                crosses += 1
    return crosses

def main():
    matrix = get_input()
    crosses = get_crosses(matrix)
    print(crosses)

if __name__ == '__main__':
    main()

