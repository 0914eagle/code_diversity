
def is_unique_columns(matrix):
    columns = [set(col) for col in zip(*matrix)]
    return len(columns) == len(set(map(tuple, columns)))

def max_rows_deleted(R, C, matrix):
    max_deleted = 0
    for i in range(R):
        if is_unique_columns(matrix[i+1:]):
            max_deleted += 1
    return max_deleted

if __name__ == '__main__':
    R, C = map(int, input().split())
    matrix = [input().strip() for _ in range(R)]
    print(max_rows_deleted(R, C, matrix))
