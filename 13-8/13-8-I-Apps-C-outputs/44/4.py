
def get_input():
    n, m = map(int, input().split())
    corridors = []
    for _ in range(m):
        u, v = map(int, input().split())
        corridors.append((u, v))
    return n, m, corridors

def remove_corridors(n, m, corridors):
    removed_corridors = set()
    while len(removed_corridors) < m // 2:
        for u, v in corridors:
            if u not in removed_corridors and v not in removed_corridors:
                removed_corridors.add(u)
                removed_corridors.add(v)
                break
    return removed_corridors

def main():
    n, m, corridors = get_input()
    removed_corridors = remove_corridors(n, m, corridors)
    print(len(removed_corridors))
    for u, v in removed_corridors:
        print(u, v)

if __name__ == '__main__':
    main()

