
def check_unique_columns(matrix):
    columns = [set(col) for col in zip(*matrix)]
    return len(columns) == len(set(columns))

def max_rows_to_delete(R, C, matrix):
    max_rows = 0
    for i in range(R):
        if check_unique_columns(matrix[i:]):
            max_rows += 1
    return max_rows

if __name__ == '__main__':
    R, C = map(int, input().split())
    matrix = [input().strip() for _ in range(R)]
    result = max_rows_to_delete(R, C, matrix)
    print(result)
