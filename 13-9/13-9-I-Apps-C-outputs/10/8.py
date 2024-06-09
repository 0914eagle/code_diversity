
def solve(R, S, G, apples):
    # Initialize a 2D array to represent the fruit garden
    garden = [[0] * S for _ in range(R)]

    # Fill the garden with trees based on the input
    for i in range(R):
        for j in range(S):
            if apples[i][j] == "x":
                garden[i][j] = 1

    # Calculate the squared distance between the apple fall and the nearest tree
    distances = []
    for i in range(G):
        r, s = apples[i]
        distance = 0
        for dr in range(-1, 2):
            for ds in range(-1, 2):
                if 0 <= r + dr < R and 0 <= s + ds < S and garden[r + dr][s + ds] == 1:
                    distance = max(distance, (dr ** 2 + ds ** 2))
        distances.append(distance)

    return distances

