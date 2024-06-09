
def solve(n, k, chips):
    # Initialize the result string
    result = ""

    # Iterate over the chips for the given number of iterations
    for i in range(k):
        # Iterate over the chips and determine the color of each chip
        for j in range(n):
            # Get the indices of the neighbors of the current chip
            neighbor_indices = get_neighbor_indices(n, j)

            # Count the number of white and black chips among the neighbors
            num_white_neighbors = 0
            num_black_neighbors = 0
            for neighbor_index in neighbor_indices:
                if chips[neighbor_index] == "W":
                    num_white_neighbors += 1
                elif chips[neighbor_index] == "B":
                    num_black_neighbors += 1

            # Determine the color of the current chip based on the number of white and black neighbors
            if num_white_neighbors > num_black_neighbors:
                result += "W"
            else:
                result += "B"

    # Return the result string
    return result

def get_neighbor_indices(n, index):
    # Handle the edge cases
    if index == 0:
        return [n-1, 1]
    elif index == n-1:
        return [n-2, 0]
    else:
        return [index-1, index+1]

n = 6
k = 1
chips = "BWBBWW"
result = solve(n, k, chips)
print(result)

n = 7
k = 3
chips = "WBWBWBW"
result = solve(n, k, chips)
print(result)

n = 6
k = 4
chips = "BWBWBW"
result = solve(n, k, chips)
print(result)

