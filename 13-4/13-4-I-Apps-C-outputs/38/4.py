
def f1(n, spots):
    # Initialize a dictionary to store the pairs of pebbles that can be jumped between
    pairs = {}
    # Iterate over the list of spots and populate the dictionary
    for i in range(n):
        for j in range(i+1, n):
            if spots[i] + spots[j] == j - i:
                pairs[i] = j
    # Initialize a list to store the distances of the pebbles that can be reached
    distances = []
    # Iterate over the dictionary and calculate the distances of the pebbles that can be reached
    for i in range(n):
        if i in pairs:
            distances.append(pairs[i] - i)
    # Return the maximum distance
    return max(distances)

def f2(n, spots):
    # Initialize a list to store the distances of the pebbles that can be reached
    distances = []
    # Iterate over the list of spots and calculate the distances of the pebbles that can be reached
    for i in range(n):
        for j in range(i+1, n):
            if spots[i] + spots[j] == j - i:
                distances.append(j - i)
    # Return the maximum distance
    return max(distances)

if __name__ == '__main__':
    n = int(input())
    spots = list(map(int, input().split()))
    print(f1(n, spots))
    print(f2(n, spots))

