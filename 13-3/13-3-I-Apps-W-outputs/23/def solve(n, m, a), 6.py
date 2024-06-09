
def solve(n, m, a):
    # Initialize a dictionary to store the number of books of each genre
    genres = {}
    for i in range(n):
        if a[i] not in genres:
            genres[a[i]] = 1
        else:
            genres[a[i]] += 1
    
    # Initialize the number of options to 0
    options = 0
    
    # Iterate over the genres and calculate the number of options for each genre
    for genre in genres:
        options += genres[genre] * (genres[genre] - 1) // 2
    
    return options

