
def count_playlists(n, T, songs):
    # Initialize a list to store the playlists
    playlists = []
    
    # Iterate over each possible playlist
    for i in range(1 << n):
        # Convert the binary representation of i to a list of song indices
        playlist = [j for j in range(n) if i & (1 << j)]
        
        # Check if the playlist is valid
        if is_valid_playlist(playlist, T, songs):
            playlists.append(playlist)
    
    # Return the number of valid playlists
    return len(playlists)

def is_valid_playlist(playlist, T, songs):
    # Check if the playlist is of the required length
    if len(playlist) != T:
        return False
    
    # Check if the playlist has no consecutive songs of the same genre
    for i in range(len(playlist) - 1):
        if songs[playlist[i]][1] == songs[playlist[i + 1]][1]:
            return False
    
    # Check if the playlist has no repeated songs
    for i in range(len(playlist) - 1):
        if playlist[i] == playlist[i + 1]:
            return False
    
    # If all checks pass, the playlist is valid
    return True

def main():
    n, T = map(int, input().split())
    songs = []
    for i in range(n):
        t, g = map(int, input().split())
        songs.append([t, g])
    print(count_playlists(n, T, songs))

if __name__ == '__main__':
    main()

