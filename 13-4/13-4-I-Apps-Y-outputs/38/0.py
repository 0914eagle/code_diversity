
def get_input():
    N, X = map(int, input().split())
    x_coordinates = list(map(int, input().split()))
    return N, X, x_coordinates

def get_max_d(N, X, x_coordinates):
    x_coordinates.sort()
    d = 1
    while d <= X:
        if all(x_coordinates[i] - x_coordinates[0] % d == 0 for i in range(1, N)):
            return d
        d += 1
    return -1

def main():
    N, X, x_coordinates = get_input()
    print(get_max_d(N, X, x_coordinates))

if __name__ == '__main__':
    main()

