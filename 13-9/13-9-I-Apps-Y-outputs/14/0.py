
def get_compressed_songs(songs, m):
    # Sort the songs by their initial size in descending order
    songs.sort(key=lambda x: x[0], reverse=True)
    # Initialize the sum of sizes and the number of songs to compress
    sum_sizes, num_songs = 0, 0
    # Iterate through the songs and add them to the sum of sizes
    for song in songs:
        sum_sizes += song[0]
        num_songs += 1
        # If the sum of sizes exceeds the capacity of the flash drive, break the loop
        if sum_sizes > m:
            break
    # If the sum of sizes is less than or equal to the capacity of the flash drive, return the number of songs to compress
    if sum_sizes <= m:
        return num_songs
    # Otherwise, return -1
    return -1

def main():
    n, m = map(int, input().split())
    songs = []
    for _ in range(n):
        a, b = map(int, input().split())
        songs.append([a, b])
    print(get_compressed_songs(songs, m))

if __name__ == '__main__':
    main()

