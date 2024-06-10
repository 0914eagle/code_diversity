
def get_rows_cols(matrix):
    rows = set()
    cols = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                rows.add(i)
                cols.add(j)
    return rows, cols

def count_white_cells(matrix, rows, cols):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i not in rows and j not in cols:
                count += 1
    return count

def main():
    h, w = map(int, input().split())
    matrix = []
    for i in range(h):
        matrix.append(list(map(int, input().split())))
    rows, cols = get_rows_cols(matrix)
    print(count_white_cells(matrix, rows, cols))

if __name__ == '__main__':
    main()

