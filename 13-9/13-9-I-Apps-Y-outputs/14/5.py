
def get_compressed_songs(songs, m):
    # Sort the songs by their initial size in descending order
    songs.sort(key=lambda x: x[0], reverse=True)
    
    # Initialize the sum of sizes and the number of compressed songs
    total_size = 0
    num_compressed = 0
    
    # Iterate through the songs and add them to the flash drive
    for song in songs:
        # If the sum of sizes is less than or equal to the flash drive capacity, add the song to the flash drive
        if total_size + song[0] <= m:
            total_size += song[0]
        # Otherwise, compress the song and add it to the flash drive
        else:
            total_size += song[1]
            num_compressed += 1
    
    # Return the number of compressed songs
    return num_compressed

def main():
    # Read the input
    n, m = map(int, input().split())
    songs = []
    for i in range(n):
        a, b = map(int, input().split())
        songs.append((a, b))
    
    # Call the get_compressed_songs function and print the result
    result = get_compressed_songs(songs, m)
    print(result)

if __name__ == '__main__':
    main()

