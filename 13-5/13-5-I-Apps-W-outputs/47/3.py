
def get_beautiful_table(n, k):
    # Initialize a matrix with zeros
    matrix = [[0] * n for _ in range(n)]
    
    # Fill in the matrix with values
    for i in range(n):
        for j in range(n):
            matrix[i][j] = (i + j) % k + 1
    
    return matrix

def main():
    n, k = map(int, input().split())
    matrix = get_beautiful_table(n, k)
    print(matrix)

if __name__ == '__main__':
    main()

