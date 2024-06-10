
def solve(n, m, songs):
    # Sort the songs by their initial size in descending order
    songs.sort(key=lambda x: x[0], reverse=True)
    
    # Initialize the sum of sizes to 0
    total_size = 0
    
    # Iterate through the songs and compress them if necessary
    for song in songs:
        if total_size + song[1] <= m:
            total_size += song[1]
        else:
            return -1
    
    # If all songs can be compressed, return the number of compressed songs
    return len(songs) - total_size

def main():
    n, m = map(int, input().split())
    songs = []
    for _ in range(n):
        a, b = map(int, input().split())
        songs.append([a, b])
    print(solve(n, m, songs))

if __name__ == '__main__':
    main()

