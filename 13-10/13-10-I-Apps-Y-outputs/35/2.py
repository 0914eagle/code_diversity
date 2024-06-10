
def get_max_value(values):
    # Initialize the maximum value as the first element
    max_value = values[0]
    # Loop through the remaining elements
    for i in range(1, len(values)):
        # Calculate the value of the new ingredient
        new_value = (values[i] + max_value) / 2
        # Update the maximum value if necessary
        if new_value > max_value:
            max_value = new_value
    return max_value

def main():
    # Read the number of ingredients and their values from stdin
    num_ingredients = int(input())
    ingredient_values = list(map(int, input().split()))
    # Get the maximum value of the last ingredient
    max_value = get_max_value(ingredient_values)
    # Print the maximum value
    print(max_value)

if __name__ == '__main__':
    main()

