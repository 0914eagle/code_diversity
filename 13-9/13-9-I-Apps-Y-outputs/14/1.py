
def get_compressed_songs(song_sizes, flash_drive_size):
    # Sort the songs by their original size in descending order
    song_sizes.sort(reverse=True)
    # Initialize the number of compressed songs to 0
    num_compressed_songs = 0
    # Initialize the total size of the compressed songs to 0
    total_compressed_size = 0
    # Iterate through the songs
    for song_size in song_sizes:
        # If the total size of the compressed songs plus the current song size is less than or equal to the flash drive size
        if total_compressed_size + song_size <= flash_drive_size:
            # Increment the number of compressed songs
            num_compressed_songs += 1
            # Add the current song size to the total compressed size
            total_compressed_size += song_size
        else:
            # If the total size of the compressed songs plus the current song size is greater than the flash drive size, break the loop
            break
    # Return the number of compressed songs
    return num_compressed_songs

def main():
    # Read the number of songs and the flash drive size from stdin
    num_songs, flash_drive_size = map(int, input().split())
    # Read the song sizes from stdin
    song_sizes = []
    for _ in range(num_songs):
        song_sizes.append(int(input()))
    # Call the get_compressed_songs function and store the result in a variable
    num_compressed_songs = get_compressed_songs(song_sizes, flash_drive_size)
    # Print the result
    print(num_compressed_songs)

if __name__ == '__main__':
    main()

