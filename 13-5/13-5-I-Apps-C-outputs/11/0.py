
def is_rearrangement_possible(num_islands, current_statues, desired_statues):
    # Initialize a dictionary to keep track of the current and desired statues
    statues = {i: current_statues[i] for i in range(num_islands)}
    
    # Loop through each island and check if the current statue is the desired statue
    for i in range(num_islands):
        if statues[i] != desired_statues[i]:
            # If the current statue is not the desired statue, find the adjacent island with the desired statue
            for j in range(i-1, i+2):
                if statues[j%num_islands] == desired_statues[i]:
                    # If an adjacent island has the desired statue, move the current statue to that island
                    statues[j%num_islands] = statues[i]
                    statues[i] = 0
                    break
    
    # Check if all the desired statues have been arranged
    for i in range(num_islands):
        if statues[i] != desired_statues[i]:
            return "NO"
    
    return "YES"

