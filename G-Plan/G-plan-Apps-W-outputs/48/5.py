
def count_unique_columns(matrix):
    columns = [set(col) for col in zip(*matrix)]
    return sum(1 for col in columns if len(col) == len(set(col)))

def max_rows_to_delete(R, C, matrix):
    max_rows = 0
    for i in range(R):
        if count_unique_columns(matrix[i:]) == C:
            max_rows = max(max_rows, R - i)
    return max_rows

if __name__ == '__main__':
    R, C = map(int, input().split())
    matrix = [input().strip() for _ in range(R)]
    result = max_rows_to_delete(R, C, matrix)
    print(result)
