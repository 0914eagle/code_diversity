
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    
    # Initialize an empty list to store the separated groups
    separated_groups = []
    
    # Initialize variables to keep track of the current group and the current position in the string
    current_group = ""
    current_pos = 0
    
    # Loop through each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, start a new group
        if char == "(":
            # If the current group is not empty, add it to the list of separated groups
            if current_group != "":
                separated_groups.append(current_group)
                current_group = ""
            # Start a new group
            current_group += char
            current_pos += 1
        # If the character is a closing parenthesis, end the current group
        elif char == ")":
            # Add the character to the current group
            current_group += char
            current_pos += 1
            # If the current group is balanced (i.e., each opening parenthesis has a matching closing parenthesis), add it to the list of separated groups
            if current_group.count("(") == current_group.count(")"):
                separated_groups.append(current_group)
                current_group = ""
        # If the character is a space, ignore it
        elif char == " ":
            current_pos += 1
        # If the character is any other character, add it to the current group
        else:
            current_group += char
            current_pos += 1
    
    # If there is still an unfinished group at the end of the string, add it to the list of separated groups
    if current_group != "":
        separated_groups.append(current_group)
    
    return separated_groups

