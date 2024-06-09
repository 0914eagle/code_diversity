
def f1(n, r, w, h):
    # Initialize variables
    gems = []
    max_gems = 0

    # Read the input
    for i in range(n):
        x, y = map(int, input().split())
        gems.append((x, y))

    # Sort the gems by their y-coordinate in descending order
    gems.sort(key=lambda x: x[1], reverse=True)

    # Loop through the gems and check if they are within reach
    for gem in gems:
        x, y = gem
        if y <= h:
            max_gems += 1
        else:
            break

    return max_gems

def f2(n, r, w, h):
    # Initialize variables
    gems = []
    max_gems = 0

    # Read the input
    for i in range(n):
        x, y = map(int, input().split())
        gems.append((x, y))

    # Sort the gems by their x-coordinate in ascending order
    gems.sort(key=lambda x: x[0])

    # Loop through the gems and check if they are within reach
    for gem in gems:
        x, y = gem
        if x >= 0 and x <= w:
            max_gems += 1
        else:
            break

    return max_gems

if __name__ == '__main__':
    n, r, w, h = map(int, input().split())
    print(f1(n, r, w, h))
    print(f2(n, r, w, h))

