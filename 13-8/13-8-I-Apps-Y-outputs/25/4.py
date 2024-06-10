
def get_input():
    N, M, X, Y = map(int, input().split())
    x_coords = list(map(int, input().split()))
    y_coords = list(map(int, input().split()))
    return N, M, X, Y, x_coords, y_coords

def check_war(N, M, X, Y, x_coords, y_coords):
    # Check if there is a common coordinate between the two empires
    common_coords = set(x_coords).intersection(set(y_coords))
    if common_coords:
        return "War"

    # Check if there is a coordinate that satisfies all three conditions
    for i in range(1, X):
        if i in x_coords and i in y_coords:
            return "No War"

    return "War"

def main():
    N, M, X, Y, x_coords, y_coords = get_input()
    print(check_war(N, M, X, Y, x_coords, y_coords))

if __name__ == '__main__':
    main()

