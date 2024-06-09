
def get_discrete_dish(w, w_i, t_i, delta_t_i):
    # Calculate the total tastiness of a discrete dish
    return (t_i - (w - w_i) * delta_t_i)

def get_continuous_dish(x, t_i, delta_t_i):
    # Calculate the total tastiness of a continuous dish
    return (t_i - x * delta_t_i)

def get_max_tastiness(dishes, w):
    # Initialize the maximum total tastiness
    max_tastiness = 0
    
    # Iterate over the dishes
    for dish in dishes:
        # Check if the dish is discrete or continuous
        if dish[0] == "D":
            # Discrete dish
            w_i = dish[1]
            t_i = dish[2]
            delta_t_i = dish[3]
            # Calculate the total tastiness of the dish
            tastiness = get_discrete_dish(w, w_i, t_i, delta_t_i)
        else:
            # Continuous dish
            t_i = dish[1]
            delta_t_i = dish[2]
            # Calculate the total tastiness of the dish
            tastiness = get_continuous_dish(w, t_i, delta_t_i)
        
        # Update the maximum total tastiness
        max_tastiness = max(max_tastiness, tastiness)
    
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

