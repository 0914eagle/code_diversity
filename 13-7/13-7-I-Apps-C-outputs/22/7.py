
def remove_ads(web_page):
    # Initialize variables
    ads_removed = 0
    image_count = 0
    image_border = '$+'
    banned_chars = ['?', '!', ',', '.', ' ']
    images = []

    # Loop through each line of the web page
    for i in range(len(web_page)):
        line = web_page[i]

        # Loop through each character in the line
        for j in range(len(line)):
            char = line[j]

            # Check if the character is part of an image border
            if char == image_border:
                # If this is the first character of an image, create a new image object
                if not images:
                    images.append([])
                    image_count += 1

                # Add the character to the current image
                images[-1].append(char)

            # Check if the character is a banned character
            elif char in banned_chars:
                # If the character is found inside an image, remove the image
                if images:
                    images[-1].append(char)
                    ads_removed += 1
                    images = []

                # If the character is not found inside an image, replace it with a whitespace
                else:
                    line = line[:j] + ' ' + line[j+1:]
                    web_page[i] = line

    # Replace the ads with whitespaces
    for image in images:
        for char in image:
            if char in banned_chars:
                ads_removed += 1
                break

    return ' '.join(web_page), ads_removed

