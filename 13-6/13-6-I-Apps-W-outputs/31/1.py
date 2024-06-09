
def solve(k, a):
    # Convert the input array to a binary string
    binary_str = "".join(str(int(x)) for x in a)
    
    # Initialize the variables
    current_day = 0
    days_spent = 0
    classes_taken = 0
    
    # Loop through the binary string
    for i in range(len(binary_str)):
        # If the current day has classes, take a class and increment the number of classes taken
        if binary_str[i] == "1":
            classes_taken += 1
        
        # If the number of classes taken is equal to the required number of classes, break the loop
        if classes_taken == k:
            break
        
        # Increment the current day and the number of days spent
        current_day = (current_day + 1) % 7
        days_spent += 1
    
    # Return the number of days spent
    return days_spent

