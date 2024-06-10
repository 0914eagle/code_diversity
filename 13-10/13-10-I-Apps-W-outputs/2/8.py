
def get_table(n, m):
    table = []
    for _ in range(n):
        row = list(map(int, input().split()))
        table.append(row)
    return table

def count_sets(table):
    n, m = len(table), len(table[0])
    sets = 0
    for i in range(n):
        for j in range(m):
            if table[i][j] == 1:
                sets += 1
                for k in range(j+1, m):
                    if table[i][k] == 1:
                        sets += 1
                for l in range(i+1, n):
                    if table[l][j] == 1:
                        sets += 1
    return sets

def main():
    n, m = map(int, input().split())
    table = get_table(n, m)
    print(count_sets(table))

if __name__ == '__main__':
    main()

