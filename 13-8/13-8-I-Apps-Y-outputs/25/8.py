
def get_input():
    N, M, X, Y = map(int, input().split())
    x_coords = list(map(int, input().split()))
    y_coords = list(map(int, input().split()))
    return N, M, X, Y, x_coords, y_coords

def find_common_value(x_coords, y_coords):
    for x in x_coords:
        for y in y_coords:
            if x == y:
                return x
    return None

def solve(N, M, X, Y, x_coords, y_coords):
    common_value = find_common_value(x_coords, y_coords)
    if common_value is not None:
        return "No War"
    else:
        return "War"

if __name__ == '__main__':
    N, M, X, Y, x_coords, y_coords = get_input()
    print(solve(N, M, X, Y, x_coords, y_coords))

