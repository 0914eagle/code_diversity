
def get_area_of_white_region(W, H, points):
    
    # Initialize the area of the white region as the entire rectangle
    area = W * H
    
    # Iterate over the points and paint the corresponding regions black
    for point, a in points:
        if a == 1:
            area -= (point * H)
        elif a == 2:
            area -= (W - point) * H
        elif a == 3:
            area -= W * (H - point)
        else:
            area -= W * point
    
    return area

def main():
    # Read the input
    W, H, N = map(int, input().split())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    
    # Calculate the area of the white region
    area = get_area_of_white_region(W, H, points)
    
    # Print the result
    print(area)

if __name__ == '__main__':
    main()

