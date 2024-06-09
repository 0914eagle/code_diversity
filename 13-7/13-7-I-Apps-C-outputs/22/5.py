
def remove_ads(web_page):
    # Initialize variables
    height, width = len(web_page), len(web_page[0])
    images = []
    ads = []

    # Loop through each character in the web page
    for i in range(height):
        for j in range(width):
            # If the current character is '$', check if it forms the border of an image
            if web_page[i][j] == '$':
                # Check if the image is valid
                if is_valid_image(web_page, i, j):
                    # If the image is valid, add it to the list of images
                    images.append((i, j))

    # Loop through each image and check if it contains any banned characters
    for image in images:
        i, j = image
        # Check if the image contains any banned characters
        if contains_banned_character(web_page, i, j):
            # If the image contains a banned character, add it to the list of ads
            ads.append(image)

    # Loop through each ad and replace its characters with whitespace
    for ad in ads:
        i, j = ad
        for k in range(i, i + 3):
            for l in range(j, j + 3):
                web_page[k][l] = ' '

    # Return the web page with all ads removed
    return web_page

# Check if the current character forms the border of an image
def is_valid_image(web_page, i, j):
    # Check if the current character is the border of an image
    if web_page[i][j] == '$':
        # Check if the image is at least 3x3 in size
        if i + 2 < len(web_page) and j + 2 < len(web_page[0]):
            # Check if the image does not contain any banned characters
            if not contains_banned_character(web_page, i, j):
                # Check if the image does not contain any other images
                if not contains_image(web_page, i, j):
                    return True

    return False

# Check if the current character contains a banned character
def contains_banned_character(web_page, i, j):
    # Check if the current character is a banned character
    if web_page[i][j] not in ['$', '+', '?', '!', ',', '.', ' ']:
        return True

    return False

# Check if the current character contains another image
def contains_image(web_page, i, j):
    # Check if the current character is the border of an image
    if web_page[i][j] == '$':
        # Check if the image is at least 3x3 in size
        if i + 2 < len(web_page) and j + 2 < len(web_page[0]):
            # Check if the image does not contain any banned characters
            if not contains_banned_character(web_page, i, j):
                # Check if the image does not contain any other images
                if not contains_image(web_page, i, j):
                    return True

    return False

