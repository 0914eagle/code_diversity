
def solve(movies, horror_list, similarities):
    # Initialize a dictionary to store the horror index for each movie
    horror_index = {}

    # Set the horror index for the movies on the horror list to 0
    for movie in horror_list:
        horror_index[movie] = 0

    # Iterate over the similarities and update the horror index for each movie
    for a, b in similarities:
        if a in horror_index and b in horror_index:
            horror_index[a] = max(horror_index[a], horror_index[b] + 1)
            horror_index[b] = max(horror_index[b], horror_index[a] + 1)

    # Find the movie with the highest horror index
    highest_horror_index = max(horror_index.values())

    # Return the movie with the highest horror index, or the movie with the lowest ID if there is a tie
    return [movie for movie, index in horror_index.items() if index == highest_horror_index][0]

