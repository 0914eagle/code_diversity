
def remove_ads(web_page):
    # Initialize variables
    height, width = len(web_page), len(web_page[0])
    ads = []

    # Iterate through the web page
    for i in range(height):
        for j in range(width):
            # Check if the current character is a border character
            if web_page[i][j] == "$":
                # Find the top-left corner of the ad
                top, left = i, j
                while web_page[top][left] == "$":
                    top -= 1
                    left -= 1
                top += 1
                left += 1

                # Find the bottom-right corner of the ad
                bottom, right = i, j
                while web_page[bottom][right] == "$":
                    bottom += 1
                    right += 1
                bottom -= 1
                right -= 1

                # Check if the ad is valid
                if (bottom - top + 1) * (right - left + 1) >= 9:
                    ads.append((top, left, bottom, right))

    # Remove the ads from the web page
    for ad in ads:
        for i in range(ad[0], ad[2] + 1):
            for j in range(ad[1], ad[3] + 1):
                web_page[i][j] = " "

    return "".join(["".join(row) for row in web_page])

