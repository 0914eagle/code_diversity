
def get_valid_positions(a, b, p):
    n = len(a)
    m = len(b)
    valid_positions = []
    for i in range(n - m + 1):
        if a[i:i+m] == b:
            valid_positions.append(i + 1)
    return valid_positions

def main():
    n, m, p = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    valid_positions = get_valid_positions(a, b, p)
    print(len(valid_positions))
    print(*valid_positions)

if __name__ == '__main__':
    main()

