
def get_input():
    N, M, X, Y = map(int, input().split())
    x_coords = list(map(int, input().split()))
    y_coords = list(map(int, input().split()))
    return N, M, X, Y, x_coords, y_coords

def find_common_coord(x_coords, y_coords):
    for x in x_coords:
        if x in y_coords:
            return x
    return None

def will_war_break_out(N, M, X, Y, x_coords, y_coords):
    common_coord = find_common_coord(x_coords, y_coords)
    if common_coord is None:
        return "War"
    if X < common_coord <= Y and all(x < common_coord for x in x_coords) and all(y >= common_coord for y in y_coords):
        return "No War"
    return "War"

def main():
    N, M, X, Y, x_coords, y_coords = get_input()
    print(will_war_break_out(N, M, X, Y, x_coords, y_coords))

if __name__ == '__main__':
    main()

