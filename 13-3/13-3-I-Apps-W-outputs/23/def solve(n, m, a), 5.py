
def solve(n, m, a):
    # Initialize a dictionary to store the number of books in each genre
    genre_count = {}
    for i in range(n):
        genre = a[i]
        if genre not in genre_count:
            genre_count[genre] = 1
        else:
            genre_count[genre] += 1

    # Initialize a variable to store the total number of options
    total_options = 1

    # Iterate over the genres and calculate the number of options for each genre
    for genre, count in genre_count.items():
        total_options *= count

    # Return the total number of options
    return total_options

