
def remove_ads(web_page):
    # Initialize variables
    H, W = len(web_page), len(web_page[0])
    ads = []

    # Loop through each character in the web page
    for i in range(H):
        for j in range(W):
            # If the character is '$', check if it forms an ad
            if web_page[i][j] == '$':
                # Check if the character forms a border of an image
                if web_page[i-1][j] == '$' and web_page[i+1][j] == '$' and web_page[i][j-1] == '$' and web_page[i][j+1] == '$':
                    # Check if the image contains any banned characters
                    banned_chars = ['?', '!', ',', '.', ' ']
                    contains_banned_char = False
                    for char in banned_chars:
                        if char in web_page[i-1:i+2, j-1:j+2].flatten():
                            contains_banned_char = True
                            break

                    # If the image contains a banned character, add it to the list of ads
                    if contains_banned_char:
                        ads.append((i-1, j-1))

    # Loop through the list of ads and replace them with whitespaces
    for ad in ads:
        web_page[ad[0]:ad[0]+3, ad[1]:ad[1]+3] = ' '

    return web_page

