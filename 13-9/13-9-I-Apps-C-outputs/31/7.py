
def solve(web_page):
    # Initialize variables
    H, W = len(web_page), len(web_page[0])
    images = []
    removed_images = []
    banned_chars = ["$", "+", "?", "!", ",", "."]

    # Iterate through the web page and find all images
    for i in range(H):
        for j in range(W):
            if web_page[i][j] == "$":
                # Found the start of an image, find its dimensions and border
                image_dimensions = find_image_dimensions(web_page, i, j)
                image_border = find_image_border(web_page, i, j, image_dimensions)
                images.append((image_border, image_dimensions))

    # Iterate through the images and remove any that contain banned characters
    for image in images:
        image_border, image_dimensions = image
        image_area = image_dimensions[0] * image_dimensions[1]
        for i in range(image_border[0], image_border[0] + image_dimensions[0]):
            for j in range(image_border[1], image_border[1] + image_dimensions[1]):
                if web_page[i][j] in banned_chars:
                    # Found a banned character, remove the image
                    removed_images.append(image)
                    break

    # Remove the images from the web page
    for image in removed_images:
        image_border, image_dimensions = image
        for i in range(image_border[0], image_border[0] + image_dimensions[0]):
            for j in range(image_border[1], image_border[1] + image_dimensions[1]):
                web_page[i][j] = " "

    return "".join(["".join(row) for row in web_page])

def find_image_dimensions(web_page, i, j):
    # Find the width and height of the image
    width, height = 1, 1
    while i + height < len(web_page) and web_page[i + height][j] == "+":
        height += 1
    while j + width < len(web_page[i]) and web_page[i][j + width] == "+":
        width += 1
    return (width, height)

def find_image_border(web_page, i, j, image_dimensions):
    # Find the border of the image
    top, bottom, left, right = i, i + image_dimensions[1], j, j + image_dimensions[0]
    while top > 0 and web_page[top - 1][j] == "+":
        top -= 1
    while bottom < len(web_page) and web_page[bottom][j] == "+":
        bottom += 1
    while left > 0 and web_page[i][left - 1] == "+":
        left -= 1
    while right < len(web_page[i]) and web_page[i][right] == "+":
        right += 1
    return (top, bottom, left, right)

