
def remove_ads(web_page):
    # Initialize a set to store the positions of all ads
    ads = set()
    
    # Iterate through each row of the web page
    for i in range(len(web_page)):
        # Iterate through each column of the current row
        for j in range(len(web_page[i])):
            # Check if the current character is a '$'
            if web_page[i][j] == '$':
                # If it is, recursively search for ads starting from this position
                search_for_ads(web_page, i, j, ads)
    
    # Iterate through the web page and remove all ads
    for i in range(len(web_page)):
        for j in range(len(web_page[i])):
            if (i, j) in ads:
                web_page[i] = web_page[i][:j] + " " * len(web_page[i][j:])
            else:
                web_page[i] = web_page[i][:j] + web_page[i][j] + " " * len(web_page[i][j+1:])
    
    # Return the updated web page with all ads removed
    return web_page

def search_for_ads(web_page, i, j, ads):
    # Check if the current position is within the bounds of the web page
    if i < 0 or i >= len(web_page) or j < 0 or j >= len(web_page[i]):
        return
    
    # Check if the current character is a '$'
    if web_page[i][j] == '$':
        # If it is, add it to the set of ads
        ads.add((i, j))
        # Recursively search for ads in all four directions
        search_for_ads(web_page, i-1, j, ads)
        search_for_ads(web_page, i+1, j, ads)
        search_for_ads(web_page, i, j-1, ads)
        search_for_ads(web_page, i, j+1, ads)

