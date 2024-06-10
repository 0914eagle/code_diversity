
def get_colored_sets(matrix):
    n = len(matrix)
    m = len(matrix[0])
    sets = []
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                sets.append([(i, j)])
    for i in range(n):
        for j in range(m):
            for set in sets:
                if (i, j) in set:
                    for k in range(n):
                        if matrix[k][j] == 1 and k not in set:
                            set.append((k, j))
                    for k in range(m):
                        if matrix[i][k] == 1 and (i, k) not in set:
                            set.append((i, k))
    return len(sets)

def main():
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    print(get_colored_sets(matrix))

if __name__ == '__main__':
    main()

