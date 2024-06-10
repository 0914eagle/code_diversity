
def compress_songs(songs, capacity):
    # Sort the songs by their original size in descending order
    songs.sort(key=lambda x: x[0], reverse=True)
    # Initialize the sum of the song sizes to 0
    total_size = 0
    # Initialize the number of songs to compress to 0
    num_songs_to_compress = 0
    # Iterate through the songs
    for song in songs:
        # If the sum of the song sizes is less than or equal to the capacity, add the song to the total size
        if total_size + song[0] <= capacity:
            total_size += song[0]
        # Otherwise, add the compressed size of the song to the total size
        else:
            total_size += song[1]
            num_songs_to_compress += 1
    # If the total size is less than or equal to the capacity, return the number of songs to compress
    if total_size <= capacity:
        return num_songs_to_compress
    # Otherwise, return -1
    else:
        return -1

def main():
    n, capacity = map(int, input().split())
    songs = []
    for _ in range(n):
        a, b = map(int, input().split())
        songs.append([a, b])
    print(compress_songs(songs, capacity))

if __name__ == '__main__':
    main()

