
def find_girl_name(N, boys, A, B):
    # Convert the list of boys to a set for faster lookup
    boys = set(boys)
    
    # Initialize the maximum distance and the girl's name
    max_dist = 0
    girl_name = 0
    
    # Iterate through the odd integers in the range [A, B]
    for i in range(A, B+1, 2):
        # If the current integer is not in the set of boys, it is a potential name for the girl
        if i not in boys:
            # Calculate the distance to the closest boy
            dist = min([abs(i - boy) for boy in boys])
            
            # If the current distance is greater than the maximum distance, update the maximum distance and the girl's name
            if dist > max_dist:
                max_dist = dist
                girl_name = i
    
    return girl_name

