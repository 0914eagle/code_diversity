
def cut_glass(w, h, n, cuts):
    # Initialize a list to store the areas of the maximum available glass fragments
    areas = []
    
    # Initialize the current area of the maximum available glass fragment
    current_area = w * h
    
    # Iterate through the cuts
    for cut in cuts:
        # If the cut is horizontal
        if cut[0] == "H":
            # Get the y-coordinate of the cut
            y = int(cut[1])
            
            # Calculate the area of the glass fragment to the left of the cut
            left_area = (w - y) * h
            
            # Calculate the area of the glass fragment to the right of the cut
            right_area = y * h
            
            # Calculate the area of the maximum available glass fragment
            current_area = max(current_area, left_area, right_area)
        
        # If the cut is vertical
        elif cut[0] == "V":
            # Get the x-coordinate of the cut
            x = int(cut[1])
            
            # Calculate the area of the glass fragment above the cut
            top_area = (w - x) * (h - x)
            
            # Calculate the area of the glass fragment below the cut
            bottom_area = x * (h - x)
            
            # Calculate the area of the maximum available glass fragment
            current_area = max(current_area, top_area, bottom_area)
    
    # Add the area of the maximum available glass fragment to the list
    areas.append(current_area)
    
    # Return the list of areas
    return areas

def main():
    # Read the input
    w, h, n = map(int, input().split())
    cuts = [input() for _ in range(n)]
    
    # Cut the glass
    areas = cut_glass(w, h, n, cuts)
    
    # Print the areas
    for area in areas:
        print(area)

if __name__ == '__main__':
    main()

