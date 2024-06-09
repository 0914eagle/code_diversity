
def remove_ads(web_page):
    # Initialize variables
    ads_removed = 0
    image_border = "$+"
    banned_characters = ["!", ",", ".", "?", " "]
    images = []

    # Iterate through the web page
    for row in range(len(web_page)):
        for col in range(len(web_page[row])):
            # Check if the current character is part of an image
            if web_page[row][col] in image_border:
                # Find the boundaries of the image
                top, bottom, left, right = find_image_boundaries(web_page, row, col)

                # Check if the image contains any banned characters
                contains_banned_character = False
                for i in range(top, bottom):
                    for j in range(left, right):
                        if web_page[i][j] in banned_characters:
                            contains_banned_character = True
                            break

                # If the image contains a banned character, add it to the list of images to remove
                if contains_banned_character:
                    images.append((top, bottom, left, right))

    # Remove the images from the web page
    for image in images:
        top, bottom, left, right = image
        for i in range(top, bottom):
            for j in range(left, right):
                web_page[i][j] = " "

    return web_page

def find_image_boundaries(web_page, row, col):
    # Find the top boundary of the image
    top = row
    while web_page[top][col] == "$":
        top -= 1

    # Find the bottom boundary of the image
    bottom = row
    while web_page[bottom][col] == "$":
        bottom += 1

    # Find the left boundary of the image
    left = col
    while web_page[row][left] == "$":
        left -= 1

    # Find the right boundary of the image
    right = col
    while web_page[row][right] == "$":
        right += 1

    return top, bottom, left, right

