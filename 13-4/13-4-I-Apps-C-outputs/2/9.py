
def f1(n, r, w, h):
    # Initialize variables
    gems = []
    max_gems = 0

    # Read input
    for i in range(n):
        x, y = map(int, input().split())
        gems.append((x, y))

    # Sort gems by y-coordinate in descending order
    gems.sort(key=lambda x: x[1], reverse=True)

    # Iterate through gems and calculate maximum number of gems that can be collected
    for i in range(n):
        gem = gems[i]
        x, y = gem[0], gem[1]
        if y <= h:
            max_gems += 1
        else:
            break

    return max_gems

def f2(n, r, w, h):
    # Initialize variables
    gems = []
    max_gems = 0

    # Read input
    for i in range(n):
        x, y = map(int, input().split())
        gems.append((x, y))

    # Sort gems by y-coordinate in descending order
    gems.sort(key=lambda x: x[1], reverse=True)

    # Iterate through gems and calculate maximum number of gems that can be collected
    for i in range(n):
        gem = gems[i]
        x, y = gem[0], gem[1]
        if y <= h:
            max_gems += 1
        else:
            break

    return max_gems

if __name__ == '__main__':
    n, r, w, h = map(int, input().split())
    print(f1(n, r, w, h))
    print(f2(n, r, w, h))

