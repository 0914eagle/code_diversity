
def get_max_candies(a, b, c):
    # Calculate the sum of the three piles
    total = a + b + c
    
    # Calculate the middle pile
    mid = (a + b) // 2
    
    # Calculate the difference between the middle pile and the smallest pile
    diff = abs(mid - min(a, b))
    
    # Calculate the maximum number of candies Alice can have
    max_candies = total - diff
    
    return max_candies

