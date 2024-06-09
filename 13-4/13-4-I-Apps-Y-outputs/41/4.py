
import sys

def get_perket(ingredients):
    # Sort the ingredients by their sourness in descending order
    ingredients.sort(key=lambda x: x[0], reverse=True)
    
    # Initialize the sourness and bitterness sums to 0
    sourness_sum = 0
    bitterness_sum = 0
    
    # Loop through the ingredients and calculate the sourness and bitterness sums
    for ingredient in ingredients:
        sourness_sum += ingredient[0]
        bitterness_sum += ingredient[1]
    
    # Calculate the absolute difference between the sourness and bitterness sums
    difference = abs(sourness_sum - bitterness_sum)
    
    # Return the smallest possible difference
    return difference

if __name__ == "__main__":
    # Read the input data from stdin
    ingredients = []
    for line in sys.stdin:
        ingredients.append(list(map(int, line.strip().split())))
    
    # Get the smallest possible difference between sourness and bitterness
    difference = get_perket(ingredients)
    
    # Print the result
    print(difference)

