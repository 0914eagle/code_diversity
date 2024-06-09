
def solve(n, a):
    # Initialize the minimum number of seconds as 0
    seconds = 0
    
    # Initialize a list to store the number of chocolates in each box
    boxes = a.copy()
    
    # Loop through each box and find the minimum number of chocolates
    while any(boxes):
        # Find the box with the minimum number of chocolates
        min_box = boxes.index(min(boxes))
        
        # If the minimum number of chocolates is not divisible by 2, return -1
        if boxes[min_box] % 2 != 0:
            return -1
        
        # Otherwise, divide the number of chocolates in the minimum box by 2
        boxes[min_box] //= 2
        
        # Increment the number of seconds
        seconds += 1
    
    # Return the minimum number of seconds
    return seconds

