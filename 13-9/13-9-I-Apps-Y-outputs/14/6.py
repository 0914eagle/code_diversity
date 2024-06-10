
def get_min_compressed_songs(songs, flash_drive_size):
    # Sort the songs by their initial size in descending order
    songs.sort(key=lambda x: x[0], reverse=True)
    
    # Initialize the sum of sizes to 0
    total_size = 0
    
    # Iterate through the songs and add their initial size to the total size
    for song in songs:
        total_size += song[0]
        
        # If the total size is greater than the flash drive size, return -1
        if total_size > flash_drive_size:
            return -1
    
    # Initialize the number of compressed songs to 0
    num_compressed_songs = 0
    
    # Iterate through the songs and check if their initial size is greater than their compressed size
    for song in songs:
        if song[0] > song[1]:
            num_compressed_songs += 1
    
    # Return the number of compressed songs
    return num_compressed_songs

def main():
    # Read the number of songs and the flash drive size
    n, m = map(int, input().split())
    
    # Read the songs
    songs = []
    for i in range(n):
        a, b = map(int, input().split())
        songs.append([a, b])
    
    # Call the get_min_compressed_songs function and print the result
    print(get_min_compressed_songs(songs, m))

if __name__ == '__main__':
    main()

