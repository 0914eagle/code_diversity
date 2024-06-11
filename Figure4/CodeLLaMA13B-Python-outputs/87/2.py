def get_row(lst, x):
    
    return sorted([(i, j) for i, lst in enumerate(lst) for j in range(len(lst) - 1, -1, -1) if lst[j] == x], key=lambda x: x[0])

if __name__