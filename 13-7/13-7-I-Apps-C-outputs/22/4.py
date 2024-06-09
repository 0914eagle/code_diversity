
def remove_ads(web_page):
    # Initialize variables
    H, W = len(web_page), len(web_page[0])
    images = []
    ads = []

    # Loop through each character in the web page
    for i in range(H):
        for j in range(W):
            # If the current character is '$', check if it forms the border of an image
            if web_page[i][j] == '$':
                # Check if the current character is part of an image
                if is_image_border(web_page, i, j):
                    # If it is, add the image to the list of images
                    images.append((i, j))

    # Loop through each image in the list of images
    for image in images:
        # Get the coordinates of the top-left and bottom-right corners of the image
        top, left = image
        bottom = top + 1
        right = left + 1
        while web_page[bottom][right] == '$':
            bottom += 1
            right += 1

        # Loop through each character in the image
        for i in range(top, bottom + 1):
            for j in range(left, right + 1):
                # If the current character is not allowed in an image, add it to the list of ads
                if web_page[i][j] not in ["?", "!", ",", ".", " ", "$"]:
                    ads.append((i, j))

    # Loop through each ad in the list of ads
    for ad in ads:
        # Get the coordinates of the ad
        i, j = ad
        # Replace the character at the ad with a whitespace
        web_page[i][j] = " "

    # Return the web page with all the ads removed
    return "".join(["".join(row) for row in web_page])

# Check if a character is part of an image
def is_image_border(web_page, i, j):
    # Check if the current character is part of an image
    if web_page[i][j] == '$':
        # Check if the current character is the top-left corner of an image
        if i == 0 or j == 0 or web_page[i - 1][j - 1] != '$':
            return True

    return False

