
def get_compressed_songs(songs, m):
    # Sort the songs by their original size in descending order
    songs.sort(key=lambda x: x[0], reverse=True)
    # Initialize the sum of sizes to 0
    total_size = 0
    # Initialize the number of compressed songs to 0
    num_compressed = 0
    # Iterate through the songs
    for song in songs:
        # Check if the sum of sizes plus the current song's original size is less than or equal to the flash drive's capacity
        if total_size + song[0] <= m:
            # Add the current song's original size to the sum of sizes
            total_size += song[0]
            # Increment the number of compressed songs
            num_compressed += 1
        else:
            # Check if the sum of sizes plus the current song's compressed size is less than or equal to the flash drive's capacity
            if total_size + song[1] <= m:
                # Add the current song's compressed size to the sum of sizes
                total_size += song[1]
                # Increment the number of compressed songs
                num_compressed += 1
            else:
                # Return -1 if it is impossible to copy all the songs
                return -1
    # Return the number of compressed songs
    return num_compressed

def main():
    # Read the number of songs and the flash drive's capacity from stdin
    n, m = map(int, input().split())
    # Read the songs' original and compressed sizes from stdin
    songs = []
    for _ in range(n):
        songs.append(list(map(int, input().split())))
    # Get the minimum number of compressed songs
    num_compressed = get_compressed_songs(songs, m)
    # Print the minimum number of compressed songs
    print(num_compressed)

if __name__ == '__main__':
    main()

