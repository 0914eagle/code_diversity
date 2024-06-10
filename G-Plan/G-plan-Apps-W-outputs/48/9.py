
def check_unique_columns(matrix):
    columns = [set(col) for col in zip(*matrix)]
    return len(columns) == len(set(columns))

def max_rows_deleted(rows, cols, matrix):
    max_deleted = 0
    for i in range(rows):
        if check_unique_columns(matrix[i+1:]):
            max_deleted += 1
    return max_deleted

if __name__ == '__main__':
    rows, cols = map(int, input().split())
    matrix = [input().strip() for _ in range(rows)]
    result = max_rows_deleted(rows, cols, matrix)
    print(result)
