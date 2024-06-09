
def remove_ads(image):
    # Initialize a set to store the positions of all ads
    ads = set()

    # Iterate through the image and check if any characters are not allowed
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] not in ["+", "!", "?", ",", ".", " ", "\n"]:
                # If a character is not allowed, mark the position as an ad
                ads.add((i, j))

    # Iterate through the image again and replace all characters in ads with whitespace
    for i in range(len(image)):
        for j in range(len(image[0])):
            if (i, j) in ads:
                image[i][j] = " "

    return image

