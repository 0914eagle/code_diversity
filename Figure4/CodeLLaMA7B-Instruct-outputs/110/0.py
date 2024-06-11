

def exchange(lst1, lst2):
    

    # Check if all the elements in lst1 are even
    if all(num % 2 == 0 for num in lst1):
        return "YES"

    # Check if all the elements in lst2 are odd
    if all(num % 2 != 0 for num in lst2):
        return "YES"

    # Check if there are any elements in common between lst1 and lst2
    if any(num in lst2 for num in lst1):
        return "YES"

    return "NO"


