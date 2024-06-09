
def get_min_heaters(n, r, house):
    # Initialize the number of heaters needed to 0
    num_heaters = 0
    
    # Iterate through the house and check if each element is warmed up by at least one heater
    for i in range(n):
        # If the element is not warmed up by any heater, increase the number of heaters needed
        if house[i] == 0:
            num_heaters += 1
    
    # Return the number of heaters needed
    return num_heaters

