
def get_max_candies(n, x, candies):
    # Initialize variables
    max_candies = 0
    current_height = x
    current_type = -1
    types = [0, 1]

    # Iterate over the candies
    for i in range(n):
        # Check if the current candy is reachable
        if candies[i][1] <= current_height:
            # Check if the current candy is of a different type than the previous one
            if candies[i][0] != current_type:
                # Eat the current candy
                current_height += candies[i][2]
                max_candies += 1
                current_type = candies[i][0]

    return max_candies

def main():
    # Read the input
    n, x = map(int, input().split())
    candies = []
    for i in range(n):
        candies.append(list(map(int, input().split())))

    # Get the maximum number of candies
    max_candies = get_max_candies(n, x, candies)

    # Print the result
    print(max_candies)

if __name__ == '__main__':
    main()

