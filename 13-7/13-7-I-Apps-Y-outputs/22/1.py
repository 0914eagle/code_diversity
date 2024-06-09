
def stable_sort(songs, sort_attributes):
    # Sort the songs initially by the first attribute
    songs.sort(key=lambda x: x[sort_attributes[0]])
    
    # Loop through the remaining attributes and sort the songs by each attribute
    for attribute in sort_attributes[1:]:
        songs.sort(key=lambda x: x[attribute], reverse=True)
    
    return songs

