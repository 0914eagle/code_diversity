
def solve(N, H, L, horror_list, similarities):
    # Initialize a dictionary to store the horror index for each movie
    horror_index = {}

    # Set the horror index for the movies on the horror list to 0
    for movie in horror_list:
        horror_index[movie] = 0

    # Iterate over the similarities and update the horror index for each movie
    for a, b in similarities:
        if a in horror_index or b in horror_index:
            continue
        if a in horror_index:
            horror_index[b] = max(horror_index[a] + 1, horror_index.get(b, 0))
        elif b in horror_index:
            horror_index[a] = max(horror_index[b] + 1, horror_index.get(a, 0))
        else:
            horror_index[a] = horror_index.get(a, 0) + 1
            horror_index[b] = horror_index.get(b, 0) + 1

    # Return the movie with the highest horror index
    return max(horror_index, key=horror_index.get)

