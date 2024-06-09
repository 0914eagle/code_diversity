
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    # Sort the list of numbers in ascending order
    numbers.sort()
    
    # Initialize the closest pair of numbers to the first two numbers in the list
    closest_pair = (numbers[0], numbers[1])
    
    # Iterate over the remaining numbers in the list
    for i in range(2, len(numbers)):
        # Calculate the absolute difference between the current number and the first number in the closest pair
        abs_diff = abs(numbers[i] - closest_pair[0])
        
        # If the absolute difference is smaller than the absolute difference between the second and third numbers in the closest pair, replace the closest pair with the current number and the first number in the closest pair
        if abs_diff < abs(closest_pair[1] - closest_pair[0]):
            closest_pair = (numbers[i], closest_pair[0])
    
    return closest_pair

