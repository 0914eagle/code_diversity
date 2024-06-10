
def get_max_candies(candies, jump_height):
    # Initialize variables
    max_candies = 0
    current_jump_height = jump_height
    current_candy_type = None
    current_candy_mass = 0

    # Iterate through the candies
    for candy in candies:
        candy_type, candy_height, candy_mass = candy

        # If the candy is within reach, and its type is different from the previous candy, and its mass is greater than the current candy mass
        if candy_height <= current_jump_height and candy_type != current_candy_type and candy_mass > current_candy_mass:
            max_candies += 1
            current_jump_height += candy_mass
            current_candy_type = candy_type
            current_candy_mass = candy_mass

    return max_candies

def main():
    n, x = map(int, input().split())
    candies = []
    for i in range(n):
        t, h, m = map(int, input().split())
        candies.append((t, h, m))
    print(get_max_candies(candies, x))

if __name__ == '__main__':
    main()

