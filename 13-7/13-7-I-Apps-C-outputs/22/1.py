
def remove_ads(web_page):
    # Initialize variables
    height, width = len(web_page), len(web_page[0])
    images = []
    visited = [[False] * width for _ in range(height)]

    # Loop through each character in the web page
    for i in range(height):
        for j in range(width):
            # If the character is '$' and not visited, find the boundary of the image and mark it as visited
            if web_page[i][j] == '$' and not visited[i][j]:
                image = find_image_boundary(web_page, i, j, visited)
                images.append(image)

    # Remove ads by replacing the characters inside the images with whitespace
    for image in images:
        for i in range(image[0], image[2] + 1):
            for j in range(image[1], image[3] + 1):
                web_page[i][j] = ' '

    return web_page

def find_image_boundary(web_page, i, j, visited):
    # Initialize the boundary of the image
    top, bottom, left, right = i, i, j, j

    # Loop through the characters in the image
    while True:
        # If the current character is '$', update the boundary and mark it as visited
        if web_page[i][j] == '$':
            top = min(top, i)
            bottom = max(bottom, i)
            left = min(left, j)
            right = max(right, j)
            visited[i][j] = True

        # If the current character is not '$', break the loop
        else:
            break

        # If the current character is not the bottom-right corner of the image, move to the next character
        if i != bottom or j != right:
            if j == right:
                i += 1
                j = left
            else:
                j += 1

    # Return the boundary of the image
    return [top, left, bottom, right]

