
import sys

def get_perket(ingredients):
    # Sort the ingredients by their sourness in descending order
    ingredients.sort(key=lambda x: x[0], reverse=True)
    
    # Initialize the total sourness and bitterness to 0
    total_sourness = 0
    total_bitterness = 0
    
    # Loop through the ingredients and calculate the total sourness and bitterness
    for ingredient in ingredients:
        total_sourness += ingredient[0]
        total_bitterness += ingredient[1]
    
    # Calculate the difference between the total sourness and bitterness
    difference = abs(total_sourness - total_bitterness)
    
    # Return the smallest possible difference
    return difference

if __name__ == '__main__':
    ingredients = []
    for _ in range(int(input())):
        ingredients.append(list(map(int, input().split())))
    print(get_perket(ingredients))

