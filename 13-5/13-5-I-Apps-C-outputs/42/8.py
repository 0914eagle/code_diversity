
def f1(n, spots):
    # Initialize a list to store the distances between pebbles
    distances = [0] * (n + 1)
    # Initialize a list to store the pairs of pebbles where Yoshi can jump
    jumps = []
    # Loop through the list of spots and calculate the distances between pebbles
    for i in range(1, n):
        distances[i] = distances[i - 1] + 1
        if spots[i] == spots[i - 1]:
            jumps.append((i - 1, i))
    # Loop through the list of jumps and calculate the maximum distance that can be reached
    max_distance = 0
    for jump in jumps:
        if distances[jump[1]] - distances[jump[0]] == spots[jump[0]]:
            max_distance = max(max_distance, distances[jump[1]])
    return max_distance

def f2(n, spots):
    # Initialize a list to store the distances between pebbles
    distances = [0] * (n + 1)
    # Initialize a list to store the pairs of pebbles where Yoshi can jump
    jumps = []
    # Loop through the list of spots and calculate the distances between pebbles
    for i in range(1, n):
        distances[i] = distances[i - 1] + 1
        if spots[i] == spots[i - 1]:
            jumps.append((i - 1, i))
    # Loop through the list of jumps and calculate the maximum distance that can be reached
    max_distance = 0
    for jump in jumps:
        if distances[jump[1]] - distances[jump[0]] == spots[jump[0]]:
            max_distance = max(max_distance, distances[jump[1]])
    return max_distance

if __name__ == '__main__':
    n = int(input())
    spots = list(map(int, input().split()))
    print(f1(n, spots))

