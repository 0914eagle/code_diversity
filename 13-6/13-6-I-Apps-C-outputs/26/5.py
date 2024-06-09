
def solve(mission_list):
    # Calculate the probability of each mission being completed successfully
    mission_probabilities = [mission / 100 for mission in mission_list]
    
    # Initialize the maximum probability to 0
    max_probability = 0
    
    # Iterate over all possible arrangements of missions and Jimmy Bonds
    for assignment in itertools.permutations(range(len(mission_list))):
        # Calculate the probability of this particular arrangement
        probability = 1
        for i in range(len(mission_list)):
            probability *= mission_probabilities[assignment[i]]
        
        # Update the maximum probability if necessary
        if probability > max_probability:
            max_probability = probability
    
    # Return the maximum probability
    return max_probability * 100

