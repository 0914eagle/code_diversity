
import sys

def get_perket(ingredients):
    # Sort the ingredients by sourness in descending order
    ingredients.sort(key=lambda x: x[0], reverse=True)
    
    # Initialize the best difference and the chosen ingredients
    best_diff = sys.maxsize
    chosen_ingredients = []
    
    # Iterate over all possible combinations of ingredients
    for i in range(len(ingredients)):
        for j in range(i+1, len(ingredients)):
            # Calculate the total sourness and bitterness of the current combination
            total_sourness = ingredients[i][0] * ingredients[j][0]
            total_bitterness = ingredients[i][1] + ingredients[j][1]
            
            # Calculate the difference between sourness and bitterness
            diff = abs(total_sourness - total_bitterness)
            
            # If the current difference is smaller than the best difference, update the best difference and the chosen ingredients
            if diff < best_diff:
                best_diff = diff
                chosen_ingredients = [ingredients[i], ingredients[j]]
    
    return chosen_ingredients

if __name__ == '__main__':
    ingredients = []
    for _ in range(int(input())):
        ingredients.append(list(map(int, input().split())))
    
    chosen_ingredients = get_perket(ingredients)
    print(chosen_ingredients[0][0] * chosen_ingredients[1][0] - chosen_ingredients[0][1] - chosen_ingredients[1][1])

