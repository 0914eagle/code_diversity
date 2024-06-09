
def remove_ads(web_page):
    # Initialize a set to store the indices of the ads
    ads = set()
    
    # Iterate through the web page
    for i in range(len(web_page)):
        for j in range(len(web_page[i])):
            # Check if the current character is a border character
            if web_page[i][j] == "$":
                # Find the top-left corner of the ad
                top, left = find_top_left_corner(web_page, i, j)
                
                # Find the bottom-right corner of the ad
                bottom, right = find_bottom_right_corner(web_page, top, left)
                
                # Add the indices of the ad to the set
                for k in range(top, bottom+1):
                    for l in range(left, right+1):
                        ads.add((k, l))
    
    # Remove the ads from the web page
    for i in range(len(web_page)):
        for j in range(len(web_page[i])):
            if (i, j) in ads:
                web_page[i][j] = " "
    
    return web_page

def find_top_left_corner(web_page, i, j):
    # Initialize the top and left indices
    top, left = i, j
    
    # Find the topmost row that contains a border character
    while top >= 0 and web_page[top][j] != "$":
        top -= 1
    
    # Find the leftmost column that contains a border character
    while left >= 0 and web_page[i][left] != "$":
        left -= 1
    
    return top, left

def find_bottom_right_corner(web_page, top, left):
    # Initialize the bottom and right indices
    bottom, right = top, left
    
    # Find the bottommost row that contains a border character
    while bottom < len(web_page) and web_page[bottom][right] != "$":
        bottom += 1
    
    # Find the rightmost column that contains a border character
    while right < len(web_page[i]) and web_page[i][right] != "$":
        right += 1
    
    return bottom, right

