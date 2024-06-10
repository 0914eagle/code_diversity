
def get_min_songs_to_compress(songs, capacity):
    # Sort the songs by their initial size in descending order
    songs.sort(key=lambda x: x[0], reverse=True)
    # Initialize the sum of sizes to 0
    total_size = 0
    # Initialize the number of songs to compress to 0
    num_songs_to_compress = 0
    # Iterate through the songs
    for song in songs:
        # If the sum of sizes is less than or equal to the capacity, add the song to the list of songs to compress
        if total_size + song[0] <= capacity:
            total_size += song[0]
            num_songs_to_compress += 1
        # Otherwise, break the loop
        else:
            break
    # Return the number of songs to compress
    return num_songs_to_compress

def main():
    # Read the number of songs and the capacity of the flash drive from stdin
    n, m = map(int, input().split())
    # Read the initial and compressed sizes of each song from stdin
    songs = []
    for i in range(n):
        a, b = map(int, input().split())
        songs.append([a, b])
    # Call the get_min_songs_to_compress function and print the result
    print(get_min_songs_to_compress(songs, m))

if __name__ == '__main__':
    main()

