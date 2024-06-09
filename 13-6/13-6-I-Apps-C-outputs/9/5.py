
def get_rectangle_coordinates(x1, y1, x2, y2):
    
    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2)
    max_y = max(y1, y2)
    return [min_x, min_y, max_x, max_y]

def get_rectangle_area(rectangle):
    
    return (rectangle[2] - rectangle[0]) * (rectangle[3] - rectangle[1])

def get_rectangle_overlap(rectangle1, rectangle2):
    
    x1, y1, x2, y2 = rectangle1
    x3, y3, x4, y4 = rectangle2
    overlap_x = max(0, min(x2, x4) - max(x1, x3))
    overlap_y = max(0, min(y2, y4) - max(y1, y3))
    return overlap_x * overlap_y

def get_min_moves(file_coordinates, delete_coordinates):
    
    # Initialize the minimum number of moves to 0
    min_moves = 0
    # Loop through each file coordinate
    for file_coordinate in file_coordinates:
        # Check if the file coordinate is inside the delete rectangle
        if get_rectangle_overlap(delete_coordinates, get_rectangle_coordinates(*file_coordinate)) > 0:
            # If it is, increase the minimum number of moves by 1
            min_moves += 1
    return min_moves

def main():
    # Read the input data
    n_r, n_c, n, m = map(int, input().split())
    file_coordinates = [tuple(map(int, input().split())) for _ in range(n+m)]
    delete_coordinates = get_rectangle_coordinates(*file_coordinates[:n])
    # Calculate the minimum number of moves
    min_moves = get_min_moves(file_coordinates, delete_coordinates)
    # Print the result
    print(min_moves)

if __name__ == '__main__':
    main()

