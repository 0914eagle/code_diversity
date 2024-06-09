
def solve(names, a, b):
    # Find the closest even integer to the average of the names
    average = sum(names) / len(names)
    closest_even = int(round(average))
    
    # Find the closest odd integer to the average of the names
    average = sum(names) / len(names)
    closest_odd = int(round(average + 0.5))
    
    # Return the closest odd integer that is within the given range
    if a <= closest_odd <= b:
        return closest_odd
    else:
        return closest_even

