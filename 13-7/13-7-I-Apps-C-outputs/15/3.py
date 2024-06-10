
def find_matching(n, top_left_corners, bottom_right_corners):
    # Initialize a list to store the matching
    matching = []
    
    # Loop through each corner pair
    for i in range(n):
        # Find the top-left corner and bottom-right corner for the current pair
        top_left = top_left_corners[i]
        bottom_right = bottom_right_corners[i]
        
        # Check if the current corner pair is valid
        if is_valid_corner_pair(top_left, bottom_right, matching):
            # Add the current corner pair to the matching
            matching.append((top_left, bottom_right))
        else:
            # If the current corner pair is not valid, return "syntax error"
            return "syntax error"
    
    # If all corner pairs are valid, return the matching
    return matching

def is_valid_corner_pair(top_left, bottom_right, matching):
    # Check if the current corner pair is valid by checking if the borders of the current pair overlap with any other corner pair in the matching
    for pair in matching:
        if do_borders_overlap(top_left, bottom_right, pair):
            return False
    return True

def do_borders_overlap(top_left_1, bottom_right_1, top_left_2, bottom_right_2):
    # Check if the borders of the two corner pairs overlap by checking if any of the borders are the same
    return (top_left_1 == top_left_2 or top_left_1 == bottom_right_2 or bottom_right_1 == top_left_2 or bottom_right_1 == bottom_right_2)

if __name__ == '__main__':
    # Read the input
    n = int(input())
    top_left_corners = []
    bottom_right_corners = []
    for i in range(n):
        r, c = map(int, input().split())
        top_left_corners.append((r, c))
        bottom_right_corners.append((r, c))
    
    # Find the matching
    matching = find_matching(n, top_left_corners, bottom_right_corners)
    
    # Print the output
    if matching == "syntax error":
        print(matching)
    else:
        for pair in matching:
            print(top_left_corners.index(pair[0]) + 1, bottom_right_corners.index(pair[1]) + 1)

