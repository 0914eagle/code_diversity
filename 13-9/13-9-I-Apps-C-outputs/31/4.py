
def remove_ads(web_page):
    # Initialize variables
    ads_removed = 0
    images = []
    border_char = "$"
    banned_chars = ["!", ",", ".", "?"]
    whitespace = " "

    # Loop through each row of the web page
    for i in range(len(web_page)):
        # Loop through each column of the web page
        for j in range(len(web_page[i])):
            # Check if the current character is a border character
            if web_page[i][j] == border_char:
                # Find the coordinates of the top-left corner of the image
                top_left_row, top_left_col = find_top_left_corner(web_page, i, j)
                # Find the coordinates of the bottom-right corner of the image
                bottom_right_row, bottom_right_col = find_bottom_right_corner(web_page, top_left_row, top_left_col)
                # Check if the image is valid
                if is_valid_image(web_page, top_left_row, top_left_col, bottom_right_row, bottom_right_col):
                    # Add the image to the list of images
                    images.append((top_left_row, top_left_col, bottom_right_row, bottom_right_col))

    # Loop through each image and check if it contains any banned characters
    for image in images:
        # Get the coordinates of the top-left and bottom-right corners of the image
        top_left_row, top_left_col, bottom_right_row, bottom_right_col = image
        # Loop through each row of the image
        for i in range(top_left_row, bottom_right_row+1):
            # Loop through each column of the image
            for j in range(top_left_col, bottom_right_col+1):
                # Check if the current character is a banned character
                if web_page[i][j] in banned_chars:
                    # Flag the image as an ad and remove it from the web page
                    ads_removed += 1
                    web_page[i][j] = whitespace

    # Return the web page with all the ads removed
    return web_page

def find_top_left_corner(web_page, row, col):
    # Find the top-left corner of the image by moving up and left from the current position
    while row > 0 and col > 0 and web_page[row][col] == border_char:
        row -= 1
        col -= 1
    return row, col

def find_bottom_right_corner(web_page, row, col):
    # Find the bottom-right corner of the image by moving down and right from the current position
    while row < len(web_page) and col < len(web_page[row]) and web_page[row][col] == border_char:
        row += 1
        col += 1
    return row-1, col-1

def is_valid_image(web_page, top_left_row, top_left_col, bottom_right_row, bottom_right_col):
    # Check if the image is valid by checking if it is at least 3x3, has no adjacent borders, and does not contain any characters that are not allowed
    if (bottom_right_row - top_left_row < 2) or (bottom_right_col - top_left_col < 2):
        return False
    for i in range(top_left_row, bottom_right_row+1):
        for j in range(top_left_col, bottom_right_col+1):
            if web_page[i][j] != border_char and web_page[i][j] not in ["!", ",", ".", "?"]:
                return False
    return True

