
def remove_ads(web_page):
    # Initialize variables
    ads_removed = 0
    image_border = "$+"
    allowed_characters = [" ", "?", "!", ",", "."]
    banned_characters = ["#"]

    # Loop through each line of the web page
    for y in range(len(web_page)):
        line = web_page[y]

        # Loop through each character in the line
        for x in range(len(line)):
            character = line[x]

            # Check if the character is part of an image
            if character == image_border:
                # Find the boundaries of the image
                top, bottom, left, right = find_image_boundaries(web_page, x, y)

                # Check if the image contains any banned characters
                contains_banned_character = False
                for banned_character in banned_characters:
                    if banned_character in web_page[top:bottom+1, left:right+1]:
                        contains_banned_character = True
                        break

                # If the image contains a banned character, remove it
                if contains_banned_character:
                    # Replace the image with whitespace
                    web_page[top:bottom+1, left:right+1] = " "
                    ads_removed += 1

    # Return the web page with all ads removed
    return web_page

# Find the boundaries of an image
def find_image_boundaries(web_page, x, y):
    # Initialize the boundaries
    top = y
    bottom = y
    left = x
    right = x

    # Loop through the rows above the current row
    for i in range(y-1, -1, -1):
        # Check if the current row contains the image border
        if web_page[i, x] == image_border:
            # Update the top boundary
            top = i
            break

    # Loop through the rows below the current row
    for i in range(y+1, len(web_page)):
        # Check if the current row contains the image border
        if web_page[i, x] == image_border:
            # Update the bottom boundary
            bottom = i
            break

    # Loop through the columns to the left of the current column
    for i in range(x-1, -1, -1):
        # Check if the current column contains the image border
        if web_page[y, i] == image_border:
            # Update the left boundary
            left = i
            break

    # Loop through the columns to the right of the current column
    for i in range(x+1, len(web_page[0])):
        # Check if the current column contains the image border
        if web_page[y, i] == image_border:
            # Update the right boundary
            right = i
            break

    # Return the boundaries
    return top, bottom, left, right

