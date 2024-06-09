
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    # Sort the list in ascending order
    numbers.sort()
    # Initialize the closest distance between the first two numbers
    closest_distance = numbers[1] - numbers[0]
    # Initialize the closest pair as the first two numbers
    closest_pair = (numbers[0], numbers[1])
    # Iterate over the list starting from the third element
    for i in range(2, len(numbers)):
        # Calculate the distance between the current number and the previous number
        distance = numbers[i] - numbers[i-1]
        # If the distance is closer than the current closest distance, update the closest distance and closest pair
        if distance < closest_distance:
            closest_distance = distance
            closest_pair = (numbers[i-1], numbers[i])
    return closest_pair

