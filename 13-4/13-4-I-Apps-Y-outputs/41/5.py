
import sys

def get_perket(ingredients):
    # Sort the ingredients by their sourness in descending order
    ingredients.sort(key=lambda x: x[0], reverse=True)
    
    # Initialize the minimum difference between sourness and bitterness
    min_diff = 1000000000
    
    # Iterate over all possible combinations of ingredients
    for i in range(len(ingredients)):
        for j in range(i+1, len(ingredients)):
            # Calculate the total sourness and bitterness of the current combination
            total_sourness = ingredients[i][0] * ingredients[j][0]
            total_bitterness = ingredients[i][1] + ingredients[j][1]
            
            # Calculate the absolute difference between sourness and bitterness
            diff = abs(total_sourness - total_bitterness)
            
            # Update the minimum difference if necessary
            if diff < min_diff:
                min_diff = diff
    
    return min_diff

if __name__ == '__main__':
    ingredients = []
    for _ in range(int(input())):
        ingredients.append(list(map(int, input().split())))
    print(get_perket(ingredients))

