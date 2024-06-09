
def solve(n, m, a):
    # Initialize a dictionary to store the number of books in each genre
    genre_count = {}
    for i in range(n):
        genre = a[i]
        if genre not in genre_count:
            genre_count[genre] = 1
        else:
            genre_count[genre] += 1
    
    # Initialize a variable to store the number of options
    options = 0
    
    # Iterate over the dictionary and calculate the number of options
    for genre1, count1 in genre_count.items():
        for genre2, count2 in genre_count.items():
            if genre1 != genre2:
                options += count1 * count2
    
    return options

