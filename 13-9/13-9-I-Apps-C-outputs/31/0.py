
def solve(page):
    # Initialize variables
    ads = []
    height, width = len(page), len(page[0])
    
    # Iterate through the page
    for i in range(height):
        for j in range(width):
            # Check if the current character is part of an ad
            if page[i][j] in ["+", "#", "!", "?", ",", ".", " "]:
                # Find the boundary of the ad
                ad_boundary = find_boundary(page, i, j)
                if ad_boundary:
                    # Add the ad to the list of ads
                    ads.append(ad_boundary)
    
    # Remove the ads from the page
    for ad in ads:
        page = remove_ad(page, ad)
    
    return page

def find_boundary(page, i, j):
    # Initialize the boundary of the ad
    boundary = []
    
    # Check if the current character is part of an ad
    if page[i][j] in ["+", "#", "!", "?", ",", ".", " "]:
        # Add the current character to the boundary
        boundary.append((i, j))
        
        # Check if the ad is at least 3x3
        if len(boundary) < 9:
            # Find the adjacent characters that are also part of the ad
            for (x, y) in boundary:
                for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= x + dx < len(page) and 0 <= y + dy < len(page[0]) and page[x + dx][y + dy] in ["+", "#", "!", "?", ",", ".", " "]:
                        boundary.append((x + dx, y + dy))
        
        # Check if the ad is not inside another ad
        if len(boundary) >= 9 and all(page[x][y] == "+" for (x, y) in boundary):
            return boundary
    
    return None

def remove_ad(page, ad_boundary):
    # Initialize the removed characters
    removed_chars = []
    
    # Remove the ad from the page
    for (i, j) in ad_boundary:
        page[i][j] = " "
        removed_chars.append((i, j))
    
    # Remove any additional characters that are part of the ad
    for (i, j) in removed_chars:
        for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= i + dx < len(page) and 0 <= j + dy < len(page[0]) and (i + dx, j + dy) not in removed_chars and page[i + dx][j + dy] in ["+", "#", "!", "?", ",", ".", " "]:
                page[i + dx][j + dy] = " "
                removed_chars.append((i + dx, j + dy))
    
    return page

