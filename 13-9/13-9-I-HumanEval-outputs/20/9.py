
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    
    # Initialize an empty list to store the separate groups
    groups = []
    
    # Iterate through the input string
    for i in range(len(paren_string)):
        # Check if the current character is an opening parentheses
        if paren_string[i] == '(':
            # If it is, start a new group
            group = ''
            
            # Iterate through the rest of the string
            for j in range(i+1, len(paren_string)):
                # Add the current character to the group
                group += paren_string[j]
                
                # If the current character is a closing parentheses, the group is complete
                if paren_string[j] == ')':
                    # Add the group to the list of groups
                    groups.append(group)
                    # Break out of the inner loop
                    break
    
    # Return the list of groups
    return groups

