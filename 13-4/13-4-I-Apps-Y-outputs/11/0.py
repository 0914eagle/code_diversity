
def get_horror_index(movie_list, horror_list, similarities):
    # Initialize the Horror Index for each movie
    horror_index = {movie: 0 for movie in movie_list}

    # Set the Horror Index for movies on the horror list to infinity
    for movie in horror_list:
        horror_index[movie] = float('inf')

    # Update the Horror Index for movies that are similar to horrible movies
    for a, b in similarities:
        if horror_index[a] == 0:
            continue
        horror_index[b] = max(horror_index[b], horror_index[a] + 1)

    # Return the movie with the highest Horror Index
    return max(horror_index, key=horror_index.get)

