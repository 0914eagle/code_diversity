
def get_possible_values(y, k, n):
    possible_values = []
    for x in range(1, n+1):
        if (x + y) % k == 0 and x + y <= n:
            possible_values.append(x)
    return possible_values

def main():
    y, k, n = map(int, input().split())
    possible_values = get_possible_values(y, k, n)
    if possible_values:
        print(*possible_values)
    else:
        print(-1)

if __name__ == '__main__':
    main()

