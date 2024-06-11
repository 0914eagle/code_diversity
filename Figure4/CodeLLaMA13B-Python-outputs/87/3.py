def get_row(lst, x):
    
    return sorted([(i, j) for i, row in enumerate(lst) for j in range(len(row)) if lst[i][j] == x], key=lambda x: (x[0], -x[1]))

if __name__ == '