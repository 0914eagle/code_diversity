
def solve(web_page):
    # Initialize variables
    ads_removed = 0
    image_border = "$+$"
    allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789?!, "

    # Loop through the web page
    for i in range(len(web_page)):
        for j in range(len(web_page[i])):
            # Check if the current character is part of an ad
            if web_page[i][j] not in allowed_chars:
                # Find the border of the ad
                ad_border = find_border(web_page, i, j)
                # Check if the ad is the smallest ad found so far
                if ad_border[0] * ad_border[1] < min_ad_size:
                    min_ad_size = ad_border[0] * ad_border[1]
                    ad_start = (ad_border[2], ad_border[3])
                    ad_end = (ad_border[4], ad_border[5])

                # Remove the ad from the web page
                remove_ad(web_page, ad_start, ad_end)
                ads_removed += 1

    return web_page

def find_border(web_page, i, j):
    # Initialize variables
    top = i
    bottom = i
    left = j
    right = j
    found_top = False
    found_bottom = False
    found_left = False
    found_right = False

    # Find the border of the ad
    while not found_top or not found_bottom or not found_left or not found_right:
        # Check if the current character is part of the ad border
        if web_page[i][j] == image_border:
            # Check if the current character is part of the top border
            if not found_top:
                top = i
                found_top = True
            # Check if the current character is part of the bottom border
            if not found_bottom:
                bottom = i
                found_bottom = True
            # Check if the current character is part of the left border
            if not found_left:
                left = j
                found_left = True
            # Check if the current character is part of the right border
            if not found_right:
                right = j
                found_right = True

        # Move to the next character
        i += 1
        j += 1

    # Return the border of the ad
    return (top, bottom, left, right)

def remove_ad(web_page, ad_start, ad_end):
    # Initialize variables
    row_start = ad_start[0]
    row_end = ad_end[0]
    col_start = ad_start[1]
    col_end = ad_end[1]

    # Remove the ad from the web page
    for i in range(row_start, row_end + 1):
        for j in range(col_start, col_end + 1):
            web_page[i][j] = " "

    return web_page

