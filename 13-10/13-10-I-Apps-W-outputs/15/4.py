
def get_crosses(matrix):
    n = len(matrix)
    m = len(matrix[0])
    count = 0
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if matrix[i][j] == 'X' and all(matrix[i][j-1:j+2] + matrix[i-1:i+2, j] == 'XXXXX'):
                count += 1
    return count

def main():
    n = int(input())
    matrix = [input() for _ in range(n)]
    print(get_crosses(matrix))

if __name__ == '__main__':
    main()

