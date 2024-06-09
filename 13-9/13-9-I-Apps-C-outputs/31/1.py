
def remove_ads(image):
    # Initialize a set to store the positions of the '$' characters
    border_positions = set()
    
    # Iterate through the image and find all positions of '$' characters
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] == '$':
                border_positions.add((i, j))
    
    # Initialize a set to store the positions of the ads
    ad_positions = set()
    
    # Iterate through the border positions and find all positions of ads
    for i, j in border_positions:
        # Check if the current position is the top-left corner of an ad
        if image[i][j] == '$' and image[i+1][j] == '$' and image[i][j+1] == '$':
            # Find the bottom-right corner of the ad
            bottom_right_corner = find_bottom_right_corner(image, i, j)
            # Add the positions of the ad to the set of ad positions
            ad_positions.add((i, j, bottom_right_corner[0], bottom_right_corner[1]))
    
    # Initialize a list to store the positions of the characters to be replaced with whitespace
    replace_positions = []
    
    # Iterate through the ad positions and find all positions of characters to be replaced with whitespace
    for i, j, bottom_i, bottom_j in ad_positions:
        # Add the positions of the characters inside the ad to the list of positions to be replaced
        for k in range(i+1, bottom_i):
            for l in range(j+1, bottom_j):
                replace_positions.append((k, l))
    
    # Replace the characters with whitespace
    for i, j in replace_positions:
        image[i][j] = ' '
    
    return image

def find_bottom_right_corner(image, top_i, top_j):
    # Initialize the bottom-right corner as the top-right corner
    bottom_i, bottom_j = top_i, top_j
    
    # Iterate through the image and find the bottom-right corner of the ad
    for i in range(top_i+1, len(image)):
        for j in range(top_j+1, len(image[0])):
            if image[i][j] == '$':
                bottom_i, bottom_j = i, j
                break
    
    return bottom_i, bottom_j

