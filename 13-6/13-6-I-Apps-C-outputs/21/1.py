
def get_max_tastiness(dishes, w):
    # Initialize the maximum total tastiness as 0
    max_tastiness = 0
    
    # Iterate over each dish
    for dish in dishes:
        # Check if the dish is discrete or continuous
        if dish[0] == "D":
            # Discrete dish
            # Get the weight and initial tastiness of the dish
            weight, tastiness, decay = dish[1], dish[2], dish[3]
            
            # Calculate the total tastiness of the dish
            total_tastiness = tastiness - (weight - 1) * decay
            
            # Check if the dish can be added to the meal
            if total_tastiness > 0 and weight <= w:
                # Add the dish to the meal
                max_tastiness += total_tastiness
                w -= weight
        else:
            # Continuous dish
            # Get the initial tastiness and decay of the dish
            tastiness, decay = dish[1], dish[2]
            
            # Calculate the total tastiness of the dish
            total_tastiness = tastiness - w * decay
            
            # Check if the dish can be added to the meal
            if total_tastiness > 0:
                # Add the dish to the meal
                max_tastiness += total_tastiness
                w = 0
    
    # Return the maximum total tastiness
    return max_tastiness

def main():
    # Read the input
    d, w = map(int, input().split())
    dishes = []
    for _ in range(d):
        dish = input().split()
        dishes.append(dish)
    
    # Calculate the maximum total tastiness
    max_tastiness = get_max_tastiness(dishes, w)
    
    # Print the result
    print(max_tastiness)

if __name__ == '__main__':
    main()

