
def get_max_value(ingredients):
    # Initialize the maximum value as the first ingredient
    max_value = ingredients[0]
    for i in range(1, len(ingredients)):
        # Calculate the value of the new ingredient by adding the current ingredient to the maximum value
        new_value = (ingredients[i] + max_value) / 2
        # Update the maximum value if the new ingredient has a higher value
        if new_value > max_value:
            max_value = new_value
    return max_value

def main():
    # Read the number of ingredients and their values from stdin
    num_ingredients = int(input())
    ingredients = [int(input()) for _ in range(num_ingredients)]
    # Calculate the maximum value of the last ingredient
    max_value = get_max_value(ingredients)
    # Print the maximum value
    print(max_value)

if __name__ == '__main__':
    main()

