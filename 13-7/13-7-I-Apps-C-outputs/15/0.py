
def parse_rectangles(n, corners):
    # Initialize an empty dictionary to store the rectangle pairs
    rectangle_pairs = {}
    
    # Iterate through the corner pairs
    for i in range(n):
        # Get the current corner pair
        corner1, corner2 = corners[i]
        
        # Check if the current corner pair is already in the dictionary
        if corner1 in rectangle_pairs:
            # If it is, add the current corner pair to the value list
            rectangle_pairs[corner1].append(corner2)
        else:
            # If it's not, create a new key-value pair in the dictionary
            rectangle_pairs[corner1] = [corner2]
    
    # Initialize an empty list to store the final rectangle pairs
    final_rectangle_pairs = []
    
    # Iterate through the dictionary
    for key, value in rectangle_pairs.items():
        # Check if the value list has more than one element
        if len(value) > 1:
            # If it does, return a syntax error
            return "syntax error"
        else:
            # If it doesn't, add the key-value pair to the final list
            final_rectangle_pairs.append((key, value[0]))
    
    # Sort the final list by the first element of each tuple
    final_rectangle_pairs.sort(key=lambda x: x[0])
    
    # Return the final list of rectangle pairs
    return final_rectangle_pairs

def main():
    # Read the number of corner pairs and the corner coordinates from stdin
    n = int(input())
    corners = []
    for i in range(n):
        r, c = map(int, input().split())
        corners.append((r, c))
    
    # Call the parse_rectangles function and print the result
    result = parse_rectangles(n, corners)
    if result == "syntax error":
        print("syntax error")
    else:
        for i, (corner1, corner2) in enumerate(result, 1):
            print(i)

if __name__ == '__main__':
    main()

