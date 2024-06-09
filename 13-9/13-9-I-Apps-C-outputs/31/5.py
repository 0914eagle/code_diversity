
def remove_ads(web_page):
    # Initialize variables
    height, width = len(web_page), len(web_page[0])
    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789?,! .")
    ads = []

    # Loop through each row of the web page
    for row in range(height):
        # Loop through each column of the web page
        for col in range(width):
            # Check if the current character is part of an ad
            if web_page[row][col] == "$":
                # Find the boundaries of the ad
                ad_boundaries = find_ad_boundaries(web_page, row, col)
                # Check if the ad is valid
                if is_valid_ad(web_page, ad_boundaries):
                    # Add the ad to the list of ads
                    ads.append(ad_boundaries)

    # Loop through the list of ads and remove them from the web page
    for ad in ads:
        for row in range(ad[0], ad[2] + 1):
            for col in range(ad[1], ad[3] + 1):
                web_page[row][col] = " "

    return "".join(["".join(row) for row in web_page])

def find_ad_boundaries(web_page, row, col):
    # Initialize the boundaries of the ad
    top, bottom, left, right = row, row, col, col

    # Expand the boundaries of the ad to the top, bottom, left, and right until we find the edge of the ad
    while web_page[top][col] == "$":
        top -= 1
    while web_page[bottom][col] == "$":
        bottom += 1
    while web_page[row][left] == "$":
        left -= 1
    while web_page[row][right] == "$":
        right += 1

    # Return the boundaries of the ad
    return (top, bottom, left, right)

def is_valid_ad(web_page, ad_boundaries):
    # Check if the ad is at least 3x3 in size
    if (ad_boundaries[2] - ad_boundaries[0] + 1 < 3 or ad_boundaries[3] - ad_boundaries[1] + 1 < 3):
        return False

    # Check if the ad contains any characters that are not allowed
    for row in range(ad_boundaries[0], ad_boundaries[2] + 1):
        for col in range(ad_boundaries[1], ad_boundaries[3] + 1):
            if web_page[row][col] not in allowed_chars:
                return False

    # Check if the ad is not inside another ad
    for ad in ads:
        if ad != ad_boundaries and does_ad_intersect(ad, ad_boundaries):
            return False

    # Check if the ad is not adjacent to the border of the web page
    if ad_boundaries[0] == 0 or ad_boundaries[1] == 0 or ad_boundaries[2] == height - 1 or ad_boundaries[3] == width - 1:
        return False

    # If all checks pass, the ad is valid
    return True

def does_ad_intersect(ad1, ad2):
    # Check if the ads have any common rows or columns
    for row in range(min(ad1[0], ad2[0]), max(ad1[2], ad2[2]) + 1):
        for col in range(min(ad1[1], ad2[1]), max(ad1[3], ad2[3]) + 1):
            if row in range(ad1[0], ad1[2] + 1) and col in range(ad1[1], ad1[3] + 1):
                return True
    return False

