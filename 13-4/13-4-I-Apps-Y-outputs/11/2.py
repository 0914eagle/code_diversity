
def solve(N, H, L, horror_list, similarities):
    # Initialize a dictionary to store the horror index for each movie
    horror_index = {}

    # Set the horror index for the movies on the horror list to 0
    for movie in horror_list:
        horror_index[movie] = 0

    # Iterate over the similarities and update the horror index for each movie
    for a, b in similarities:
        if a in horror_index or b in horror_index:
            if a not in horror_index:
                horror_index[a] = horror_index[b] + 1
            elif b not in horror_index:
                horror_index[b] = horror_index[a] + 1
            else:
                horror_index[a] = max(horror_index[a], horror_index[b] + 1)
                horror_index[b] = max(horror_index[a], horror_index[b] + 1)

    # Find the movie with the highest horror index
    highest_horror_index = 0
    highest_horror_index_movie = 0
    for movie, horror_index in horror_index.items():
        if horror_index > highest_horror_index:
            highest_horror_index = horror_index
            highest_horror_index_movie = movie

    return highest_horror_index_movie

