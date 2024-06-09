
def get_matrix_size(input_string):
    return int(input_string)

def get_matrix_entries(input_string):
    matrix_size = get_matrix_size(input_string)
    matrix_entries = []
    for i in range(matrix_size):
        matrix_entries.append(list(map(int, input_string.split())))
    return matrix_entries

def get_matrix_values(matrix_entries):
    matrix_size = len(matrix_entries)
    matrix_values = {}
    for i in range(matrix_size):
        for j in range(matrix_size):
            if i == 0 or j == 0:
                matrix_values[(i, j)] = matrix_entries[i][j]
            else:
                matrix_values[(i, j)] = mex(matrix_values[(i-1, j)], matrix_values[(i, j-1)])
    return matrix_values

def mex(x, y):
    if x == 0 and y == 0:
        return 1
    elif x == 0 and y == 1:
        return 2
    elif x == 0 and y == 2:
        return 0
    elif x == 1 and y == 0:
        return 2
    elif x == 1 and y == 1:
        return 0
    elif x == 1 and y == 2:
        return 1
    elif x == 2 and y == 0:
        return 0
    elif x == 2 and y == 1:
        return 1
    elif x == 2 and y == 2:
        return 2

def count_values(matrix_values):
    count_0 = 0
    count_1 = 0
    count_2 = 0
    for value in matrix_values.values():
        if value == 0:
            count_0 += 1
        elif value == 1:
            count_1 += 1
        elif value == 2:
            count_2 += 1
    return count_0, count_1, count_2

def main():
    matrix_size = get_matrix_size(input())
    matrix_entries = get_matrix_entries(input())
    matrix_values = get_matrix_values(matrix_entries)
    count_0, count_1, count_2 = count_values(matrix_values)
    print(count_0, count_1, count_2)

if __name__ == '__main__':
    main()

