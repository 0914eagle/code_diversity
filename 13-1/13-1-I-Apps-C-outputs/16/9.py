
def get_max_score(numbers):
    
    # Initialize the score and the current group of numbers
    score = 0
    current_group = numbers
    
    # While there are still numbers in the current group
    while current_group:
        # If the current group has only one number, throw it out
        if len(current_group) == 1:
            current_group.pop()
        # If the current group has more than one number, split it into two non-empty groups and give each of them to Toastman
        else:
            # Split the current group into two non-empty groups
            group1 = current_group[:len(current_group) // 2]
            group2 = current_group[len(current_group) // 2:]
            
            # Add the sum of the current group to the score
            score += sum(current_group)
            
            # Give each of the two groups to Toastman
            current_group = [group1, group2]
    
    # Return the maximum possible score
    return score

