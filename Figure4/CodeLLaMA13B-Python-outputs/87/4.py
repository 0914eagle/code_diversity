def get_row(lst, x):
    
    # your code here
    result = []
    for i, row in enumerate(lst):
        for j, col in enumerate(row):
            if col == x:
                result.append((i, j))
    return sorted(result, key=lambda x: (x[0], -x[1]))

if __name__ == '__main__':