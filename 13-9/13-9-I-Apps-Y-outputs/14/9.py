
def get_min_songs_to_compress(song_sizes, flash_drive_size):
    # Sort the songs by size in descending order
    song_sizes.sort(reverse=True)
    # Initialize the number of songs to compress to 0
    num_songs_to_compress = 0
    # Initialize the total size of the songs to compress to 0
    total_size_to_compress = 0
    # Iterate through the songs
    for song_size in song_sizes:
        # If the total size of the songs to compress plus the current song size is less than or equal to the flash drive size, add the current song size to the total size to compress and increment the number of songs to compress
        if total_size_to_compress + song_size <= flash_drive_size:
            total_size_to_compress += song_size
            num_songs_to_compress += 1
        # Otherwise, break the loop
        else:
            break
    # If the total size of the songs to compress is less than or equal to the flash drive size, return the number of songs to compress
    if total_size_to_compress <= flash_drive_size:
        return num_songs_to_compress
    # Otherwise, return -1
    else:
        return -1

def main():
    # Read the number of songs and flash drive size
    n, m = map(int, input().split())
    # Read the song sizes
    song_sizes = []
    for _ in range(n):
        song_sizes.append(int(input()))
    # Call the get_min_songs_to_compress function and print the result
    result = get_min_songs_to_compress(song_sizes, m)
    print(result)

if __name__ == '__main__':
    main()

