
def solve(n, k, chips):
    # Initialize the result string
    result = ""

    # Loop through each iteration
    for i in range(k):
        # Loop through each chip
        for j in range(n):
            # Get the neighbors of the current chip
            neighbors = get_neighbors(j, n)

            # Count the number of white and black neighbors
            num_white_neighbors = 0
            num_black_neighbors = 0
            for neighbor in neighbors:
                if chips[neighbor] == "W":
                    num_white_neighbors += 1
                else:
                    num_black_neighbors += 1

            # Check if the current chip should become white
            if num_white_neighbors > num_black_neighbors:
                result += "W"
            else:
                result += "B"

    return result

def get_neighbors(j, n):
    # Handle the edge cases
    if j == 0:
        return [n-1, 1, 2]
    elif j == n-1:
        return [j-1, n-1, 0]
    else:
        return [j-1, j+1, j+2]

n = 6
k = 1
chips = "BWBBWW"
result = solve(n, k, chips)
print(result)

