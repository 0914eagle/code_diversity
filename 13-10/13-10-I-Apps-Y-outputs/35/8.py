
def get_max_value(ingredients):
    # Initialize the maximum value to the first ingredient
    max_value = ingredients[0]
    # Iterate through the remaining ingredients
    for i in range(1, len(ingredients)):
        # Calculate the value of the new ingredient
        new_value = (ingredients[i] + max_value) / 2
        # Update the maximum value if necessary
        if new_value > max_value:
            max_value = new_value
    return max_value

def main():
    # Read the number of ingredients and their values from stdin
    N = int(input())
    ingredients = [int(x) for x in input().split()]
    # Calculate the maximum value of the last ingredient
    max_value = get_max_value(ingredients)
    # Print the result
    print(max_value)

if __name__ == '__main__':
    main()

