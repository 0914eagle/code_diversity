
def get_set(x, sets):
    if sets[x] != x:
        sets[x] = get_set(sets[x], sets)
    return sets[x]

def join_sets(x, y, sets):
    x_root = get_set(x, sets)
    y_root = get_set(y, sets)
    if x_root != y_root:
        sets[x_root] = y_root

def is_same_set(x, y, sets):
    return get_set(x, sets) == get_set(y, sets)

def main():
    N, Q = map(int, input().split())
    sets = [i for i in range(N)]
    for _ in range(Q):
        query = input()
        if query.startswith("?"):
            x, y = map(int, query.split()[1:])
            print("yes" if is_same_set(x, y, sets) else "no")
        else:
            x, y = map(int, query.split()[1:])
            join_sets(x, y, sets)

if __name__ == '__main__':
    main()

