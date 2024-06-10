
def get_compressed_songs(songs, flash_drive_size):
    # Sort the songs by their original size in descending order
    songs.sort(key=lambda x: x[0], reverse=True)
    
    # Initialize the sum of song sizes to 0
    total_size = 0
    
    # Initialize the number of compressed songs to 0
    num_compressed_songs = 0
    
    # Iterate through the songs
    for song in songs:
        # Check if the sum of song sizes is less than or equal to the flash drive size
        if total_size + song[0] <= flash_drive_size:
            # Add the original size of the song to the total size
            total_size += song[0]
        else:
            # Add the compressed size of the song to the total size
            total_size += song[1]
            # Increment the number of compressed songs
            num_compressed_songs += 1
    
    # Return the number of compressed songs
    return num_compressed_songs

def main():
    # Read the number of songs and flash drive size
    n, m = map(int, input().split())
    
    # Read the songs
    songs = []
    for _ in range(n):
        a, b = map(int, input().split())
        songs.append((a, b))
    
    # Get the number of compressed songs
    num_compressed_songs = get_compressed_songs(songs, m)
    
    # Check if it is possible to copy all the songs
    if num_compressed_songs == len(songs):
        print(-1)
    else:
        print(num_compressed_songs)

if __name__ == '__main__':
    main()

