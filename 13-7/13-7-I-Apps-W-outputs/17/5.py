
def get_possible_x_values(y, k, n):
    x_values = []
    for x in range(1, n+1):
        if (x + y) % k == 0 and x + y <= n:
            x_values.append(x)
    return x_values

def main():
    y, k, n = map(int, input().split())
    x_values = get_possible_x_values(y, k, n)
    if len(x_values) == 0:
        print(-1)
    else:
        print(*x_values)

if __name__ == '__main__':
    main()

