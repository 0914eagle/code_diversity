
def get_max_candies(n, x, candies):
    # Initialize variables
    max_candies = 0
    current_height = x
    current_type = 0
    types = [0] * n
    heights = [0] * n
    masses = [0] * n

    # Parse the input
    for i in range(n):
        types[i], heights[i], masses[i] = map(int, input().split())

    # Iterate through the candies
    for i in range(n):
        # Check if the current candy is reachable
        if heights[i] <= current_height:
            # Check if the current candy has the same type as the previous one
            if types[i] == current_type:
                continue
            # Eat the current candy
            current_height += masses[i]
            max_candies += 1
            current_type = types[i]

    return max_candies

def main():
    n, x = map(int, input().split())
    candies = []
    for i in range(n):
        candies.append(list(map(int, input().split())))
    max_candies = get_max_candies(n, x, candies)
    print(max_candies)

if __name__ == '__main__':
    main()

