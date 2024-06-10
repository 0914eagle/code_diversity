
def get_min_time(hamsters):
    # Calculate the number of hamsters that need to stand up
    num_stand_up = len(hamsters) // 2
    
    # Initialize the number of minutes as 0
    minutes = 0
    
    # Loop through the hamsters and check if they need to stand up or sit down
    for i, hamster in enumerate(hamsters):
        if hamster == "X" and i < num_stand_up:
            # If the hamster is standing and should sit down, increment the number of minutes
            minutes += 1
        elif hamster == "x" and i >= num_stand_up:
            # If the hamster is sitting and should stand up, increment the number of minutes
            minutes += 1
    
    # Return the minimum number of minutes required
    return minutes

def get_optimized_hamsters(hamsters):
    # Calculate the number of hamsters that need to stand up
    num_stand_up = len(hamsters) // 2
    
    # Initialize the optimized hamsters string
    optimized_hamsters = ""
    
    # Loop through the hamsters and check if they need to stand up or sit down
    for i, hamster in enumerate(hamsters):
        if hamster == "X" and i < num_stand_up:
            # If the hamster is standing and should sit down, add a "x" to the optimized string
            optimized_hamsters += "x"
        elif hamster == "x" and i >= num_stand_up:
            # If the hamster is sitting and should stand up, add a "X" to the optimized string
            optimized_hamsters += "X"
        else:
            # If the hamster is in its original position, add the original character to the optimized string
            optimized_hamsters += hamster
    
    # Return the optimized hamsters string
    return optimized_hamsters

if __name__ == '__main__':
    # Get the number of hamsters from the user
    num_hamsters = int(input())
    
    # Get the hamsters' positions from the user
    hamsters = input()
    
    # Calculate the minimum number of minutes required to get the desired number of standing hamsters
    minutes = get_min_time(hamsters)
    
    # Get the optimized hamsters string
    optimized_hamsters = get_optimized_hamsters(hamsters)
    
    # Print the minimum number of minutes required and the optimized hamsters string
    print(minutes)
    print(optimized_hamsters)

