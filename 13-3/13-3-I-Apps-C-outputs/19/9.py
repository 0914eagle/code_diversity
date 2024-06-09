
def count_valid_positions(a, b, p):
    n = len(a)
    m = len(b)
    count = 0
    for i in range(n - m + 1):
        if a[i:i+m] == b:
            count += 1
    return count

def find_valid_positions(a, b, p):
    n = len(a)
    m = len(b)
    positions = []
    for i in range(n - m + 1):
        if a[i:i+m] == b:
            positions.append(i + 1)
    return positions

if __name__ == '__main__':
    n, m, p = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    count = count_valid_positions(a, b, p)
    positions = find_valid_positions(a, b, p)
    print(count)
    print(*positions)

