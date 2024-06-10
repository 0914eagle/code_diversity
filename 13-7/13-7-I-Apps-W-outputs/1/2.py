
def get_max_candies(height, candies):
    # Initialize variables
    max_candies = 0
    current_height = height
    current_candy = 0
    visited_candies = set()

    # Iterate through the candies
    for candy in candies:
        # Check if the current candy is reachable
        if current_height >= candy[1]:
            # Check if the current candy has not been visited before
            if candy[0] not in visited_candies:
                # Eat the current candy and update the height
                current_height += candy[2]
                current_candy += 1
                visited_candies.add(candy[0])

    # Return the maximum number of candies eaten
    return current_candy

def get_candies(n, x, candies):
    # Initialize variables
    max_candies = 0
    current_height = x
    visited_candies = set()

    # Iterate through the candies
    for candy in candies:
        # Check if the current candy is reachable
        if current_height >= candy[1]:
            # Check if the current candy has not been visited before
            if candy[0] not in visited_candies:
                # Eat the current candy and update the height
                current_height += candy[2]
                visited_candies.add(candy[0])
                max_candies += 1

    # Return the maximum number of candies eaten
    return max_candies

def main():
    n, x = map(int, input().split())
    candies = []
    for i in range(n):
        t, h, m = map(int, input().split())
        candies.append([t, h, m])
    print(get_candies(n, x, candies))

if __name__ == '__main__':
    main()

