
def get_input():
    N, M, X, Y = map(int, input().split())
    x_coords = list(map(int, input().split()))
    y_coords = list(map(int, input().split()))
    return N, M, X, Y, x_coords, y_coords

def find_common_coord(x_coords, y_coords):
    for x in x_coords:
        for y in y_coords:
            if x == y:
                return x
    return None

def determine_outcome(X, Y, x_coords, y_coords):
    common_coord = find_common_coord(x_coords, y_coords)
    if common_coord:
        return "No War"
    else:
        if X < common_coord <= Y and all(x < common_coord for x in x_coords) and all(y >= common_coord for y in y_coords):
            return "No War"
        else:
            return "War"

def main():
    N, M, X, Y, x_coords, y_coords = get_input()
    print(determine_outcome(X, Y, x_coords, y_coords))

if __name__ == '__main__':
    main()

