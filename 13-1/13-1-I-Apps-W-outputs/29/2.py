
def count_playlists(songs, total_time):
    # Initialize a list to store the playlists
    playlists = []
    
    # Iterate over the songs
    for i in range(len(songs)):
        # Get the current song and its duration
        song = songs[i]
        duration = song[0]
        
        # Check if the song fits in the remaining time
        if duration <= total_time:
            # If the song fits, add it to the playlist
            playlists.append([song])
            
            # Subtract the song duration from the total time
            total_time -= duration
            
            # Recursively call the function to get the remaining playlists
            remaining_playlists = count_playlists(songs[i+1:], total_time)
            
            # Add the current song to all the remaining playlists
            for playlist in remaining_playlists:
                playlist.insert(0, song)
            
            # Add the current playlist to the final list of playlists
            playlists.extend(remaining_playlists)
    
    # Return the list of playlists
    return playlists

def main():
    # Read the input
    n, total_time = map(int, input().split())
    songs = []
    for i in range(n):
        t, g = map(int, input().split())
        songs.append([t, g])
    
    # Call the function to get the playlists
    playlists = count_playlists(songs, total_time)
    
    # Print the number of playlists
    print(len(playlists))

if __name__ == '__main__':
    main()

