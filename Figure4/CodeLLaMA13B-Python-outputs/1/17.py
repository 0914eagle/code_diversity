from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    
    # Hint: use stacks
    # Hint2: if you encounter '(', push to stack, if you encounter ')', pop from stack
    # Hint3: if stack is empty when you encounter ')', you have your group
    # Hint4: if stack is not empty after processing the whole string, you have unbalanced parentheses
    # Hint5: you can use list.join() to join characters in a list into a string
    # Hint6: you can use str.strip() to remove spaces from a string
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
