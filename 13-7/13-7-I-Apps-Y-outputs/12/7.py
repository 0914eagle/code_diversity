
def get_white_area(width, height, points):
    # Initialize the white area as the entire rectangle
    white_area = width * height
    
    # Loop through each point and its corresponding a value
    for point, a in points:
        # If a is 1, paint the region to the left of the point
        if a == 1:
            white_area -= point * height
        # If a is 2, paint the region to the right of the point
        elif a == 2:
            white_area -= (width - point) * height
        # If a is 3, paint the region below the point
        elif a == 3:
            white_area -= width * (height - point)
        # If a is 4, paint the region above the point
        elif a == 4:
            white_area -= width * point
    
    return white_area

def main():
    width, height, num_points = map(int, input().split())
    points = []
    for _ in range(num_points):
        x, y, a = map(int, input().split())
        points.append((x, y, a))
    print(get_white_area(width, height, points))

if __name__ == '__main__':
    main()

