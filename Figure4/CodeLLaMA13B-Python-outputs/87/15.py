def get_row(lst, x):
    
    # your code here
    result = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                result.append((i, j))
    return sorted(result, key=lambda x: (x[0], -x[1]))

if __name__ == '__main__':
    #These "asserts" using