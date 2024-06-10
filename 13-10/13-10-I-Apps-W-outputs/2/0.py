
def get_number_of_sets(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    num_sets = 0
    
    for row in range(num_rows):
        for col in range(num_cols):
            if matrix[row][col] == 1:
                num_sets += 1
                for i in range(row + 1, num_rows):
                    if matrix[i][col] == 1:
                        num_sets -= 1
                for j in range(col + 1, num_cols):
                    if matrix[row][j] == 1:
                        num_sets -= 1
    
    return num_sets

def main():
    num_rows, num_cols = map(int, input().split())
    matrix = []
    for _ in range(num_rows):
        matrix.append(list(map(int, input().split())))
    print(get_number_of_sets(matrix))

if __name__ == '__main__':
    main()

