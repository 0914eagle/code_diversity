
def remove_ads(web_page):
    # Initialize variables
    ads_removed = 0
    ads_found = False
    image_border = '$+'
    banned_chars = ['?', '!', ',', '.', ' ']
    images = []

    # Loop through each line of the web page
    for i in range(len(web_page)):
        for j in range(len(web_page[i])):
            # Check if the current character is part of an image border
            if web_page[i][j] == image_border:
                # Find the boundaries of the image
                x1, y1, x2, y2 = find_image_bounds(web_page, i, j)

                # Check if the image contains any banned characters
                contains_banned_chars = False
                for k in range(x1, x2+1):
                    for l in range(y1, y2+1):
                        if web_page[k][l] in banned_chars:
                            contains_banned_chars = True
                            break

                # If the image contains banned characters, add it to the list of ads
                if contains_banned_chars:
                    ads_found = True
                    images.append((x1, y1, x2, y2))

    # Remove the ads from the web page
    for image in images:
        x1, y1, x2, y2 = image
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                web_page[i][j] = ' '

    return web_page

def find_image_bounds(web_page, x, y):
    # Find the top-left corner of the image
    while web_page[x][y] != image_border:
        x -= 1
        y -= 1

    # Find the bottom-right corner of the image
    x1 = x2 = x
    y1 = y2 = y
    while web_page[x1][y1] == image_border:
        x1 -= 1
    x1 += 1
    while web_page[x2][y2] == image_border:
        x2 += 1
    x2 -= 1
    while web_page[x][y1] == image_border:
        y1 -= 1
    y1 += 1
    while web_page[x][y2] == image_border:
        y2 += 1
    y2 -= 1

    return x1, y1, x2, y2

