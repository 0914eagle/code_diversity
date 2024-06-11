

def exchange(lst1, lst2):
    

    # Check if all the elements of lst1 are even
    if all(num % 2 == 0 for num in lst1):
        return "YES"

    # Check if lst2 is empty
    if not lst2:
        return "NO"

    # Create a set of even numbers from lst2
    even_nums = {num for num in lst2 if num % 2 == 0}

    # Check if all the elements of lst1 are in even_nums
    if len(even_nums) == len(lst1):
        return "YES"

    # Check if there is at least one element in lst1 that is not in even_nums
    if any(num not in even_nums for num in lst1):
        return "NO"

    # If the above conditions are not met, it is possible to exchange elements between lst1 and lst2 to make all the elements of lst1 to be even
    return "YES"


