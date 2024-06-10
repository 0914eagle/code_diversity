
def get_input():
    n, m = map(int, input().split())
    table = []
    for _ in range(n):
        table.append(list(map(int, input().split())))
    return table

def get_sets(table):
    sets = []
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == 1:
                sets.append([(i, j)])
    return sets

def get_non_empty_sets(sets):
    non_empty_sets = []
    for set in sets:
        if len(set) > 1:
            non_empty_sets.append(set)
    return non_empty_sets

def count_sets(non_empty_sets):
    count = 0
    for set in non_empty_sets:
        count += len(set)
    return count

def main():
    table = get_input()
    sets = get_sets(table)
    non_empty_sets = get_non_empty_sets(sets)
    count = count_sets(non_empty_sets)
    print(count)

if __name__ == '__main__':
    main()

