
def stable_sort(songs, attributes):
    # Sort the songs by the first attribute
    songs.sort(key=lambda x: x[attributes[0]])
    
    # Loop through the remaining attributes
    for attribute in attributes[1:]:
        # Sort the songs by the current attribute, but use the previous sort order as the starting point
        songs.sort(key=lambda x: x[attribute], reverse=True)
    
    return songs

