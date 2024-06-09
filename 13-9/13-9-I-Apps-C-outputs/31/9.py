
def solve(web_page):
    # Initialize variables
    height, width = len(web_page), len(web_page[0])
    images = []
    banned_chars = ["!", "?", ",", "."]

    # Loop through each character in the web page
    for i in range(height):
        for j in range(width):
            # Check if the current character is a border character
            if web_page[i][j] == "$":
                # Find the boundaries of the image
                top, bottom, left, right = find_boundaries(web_page, i, j)

                # Check if the image contains any banned characters
                contains_banned_char = False
                for k in range(top, bottom):
                    for l in range(left, right):
                        if web_page[k][l] in banned_chars:
                            contains_banned_char = True
                            break

                # If the image contains a banned character, add it to the list of images to remove
                if contains_banned_char:
                    images.append((top, bottom, left, right))

    # Sort the images by their area (smallest first)
    images.sort(key=lambda x: (x[1] - x[0]) * (x[3] - x[2]))

    # Remove the images from the web page
    for top, bottom, left, right in images:
        for i in range(top, bottom):
            for j in range(left, right):
                web_page[i][j] = " "

    # Return the updated web page
    return "".join("".join(row) for row in web_page)

# Find the boundaries of an image given a border character
def find_boundaries(web_page, i, j):
    # Initialize variables
    top, bottom, left, right = i, i, j, j
    border_char = "$"

    # Find the top boundary
    while top > 0 and web_page[top - 1][j] == border_char:
        top -= 1

    # Find the bottom boundary
    while bottom < len(web_page) - 1 and web_page[bottom + 1][j] == border_char:
        bottom += 1

    # Find the left boundary
    while left > 0 and web_page[i][left - 1] == border_char:
        left -= 1

    # Find the right boundary
    while right < len(web_page[0]) - 1 and web_page[i][right + 1] == border_char:
        right += 1

    return top, bottom, left, right

