
def get_possible_x_values(y, k, n):
    possible_x_values = []
    for x in range(1, n//k+1):
        if (x+y) % k == 0 and x+y <= n:
            possible_x_values.append(x)
    return possible_x_values

def main():
    y, k, n = map(int, input().split())
    possible_x_values = get_possible_x_values(y, k, n)
    if possible_x_values:
        print(*possible_x_values)
    else:
        print(-1)

if __name__ == '__main__':
    main()

