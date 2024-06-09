
def remove_ads(web_page):
    # Initialize variables
    height, width = len(web_page), len(web_page[0])
    ads = []

    # Iterate through the web page
    for i in range(height):
        for j in range(width):
            # Check if the current character is a border character
            if web_page[i][j] == "$+$":
                # Find the top-left corner of the ad
                top, left = i, j
                while top > 0 and web_page[top - 1][j] == "$+$":
                    top -= 1
                while left > 0 and web_page[i][left - 1] == "$+$":
                    left -= 1

                # Find the bottom-right corner of the ad
                bottom, right = i, j
                while bottom < height - 1 and web_page[bottom + 1][j] == "$+$":
                    bottom += 1
                while right < width - 1 and web_page[i][right + 1] == "$+$":
                    right += 1

                # Check if the ad is valid
                if (right - left + 1) * (bottom - top + 1) >= 9:
                    ads.append((top, left, bottom, right))

    # Sort the ads by their size in descending order
    ads.sort(key=lambda x: (x[2] - x[0] + 1) * (x[3] - x[1] + 1), reverse=True)

    # Remove the ads from the web page
    for top, left, bottom, right in ads:
        for i in range(top, bottom + 1):
            for j in range(left, right + 1):
                web_page[i][j] = " "

    return "".join("".join(row) for row in web_page)

