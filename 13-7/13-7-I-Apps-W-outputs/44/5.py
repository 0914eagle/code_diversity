
def cut_glass(w, h, n, cuts):
    # Initialize a list to store the areas of the glass fragments
    areas = []
    
    # Set the initial area of the largest fragment to the area of the entire sheet of glass
    largest_area = w * h
    
    # Iterate through each cut
    for cut in cuts:
        # If the cut is horizontal, calculate the area of the fragment to the left and right of the cut
        if cut[0] == 'H':
            left_area = cut[1] * h
            right_area = (w - cut[1]) * h
        
        # If the cut is vertical, calculate the area of the fragment above and below the cut
        else:
            top_area = w * cut[1]
            bottom_area = w * (h - cut[1])
        
        # Calculate the area of the largest fragment by comparing the areas of the two fragments
        largest_area = max(left_area, right_area, top_area, bottom_area)
        
        # Add the area of the largest fragment to the list of areas
        areas.append(largest_area)
    
    # Return the list of areas
    return areas

def main():
    # Read the input
    w, h, n = map(int, input().split())
    cuts = [input().split() for _ in range(n)]
    
    # Call the cut_glass function and print the output
    areas = cut_glass(w, h, n, cuts)
    for area in areas:
        print(area)

if __name__ == '__main__':
    main()

