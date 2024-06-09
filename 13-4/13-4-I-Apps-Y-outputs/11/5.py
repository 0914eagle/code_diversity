
def get_horror_index(movie_list, horror_list, similarities):
    # Initialize the horror index for each movie
    horror_index = {movie: 0 for movie in movie_list}

    # Set the horror index for movies on the horror list to infinity
    for movie in horror_list:
        horror_index[movie] = float('inf')

    # Iterate through the similarities and update the horror index
    for a, b in similarities:
        if horror_index[a] < horror_index[b]:
            horror_index[a] = horror_index[b] + 1
        elif horror_index[b] < horror_index[a]:
            horror_index[b] = horror_index[a] + 1

    # Return the movie with the highest horror index
    return max(horror_index, key=horror_index.get)

