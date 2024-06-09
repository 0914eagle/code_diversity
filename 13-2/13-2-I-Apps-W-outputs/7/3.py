
def get_maximum_circular_value(numbers):
    n = len(numbers)
    if n == 1:
        return numbers[0]
    
    # initialize the maximum circular value
    max_value = 0
    
    # iterate through all possible starting indices
    for i in range(n):
        # calculate the circular value for the current starting index
        value = get_circular_value(numbers, i)
        
        # update the maximum circular value
        if value > max_value:
            max_value = value
    
    return max_value

def get_circular_value(numbers, start_index):
    n = len(numbers)
    value = 0
    
    # iterate through the circle
    for i in range(n):
        # calculate the sum of the current element and its adjacent element
        value += numbers[(start_index + i) % n] + numbers[(start_index + i + 1) % n]
    
    return value

