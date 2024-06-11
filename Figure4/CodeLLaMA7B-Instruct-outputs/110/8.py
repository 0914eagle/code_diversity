

def exchange(lst1, lst2):
    

    # Check if all the elements of lst1 are even
    if all(num % 2 == 0 for num in lst1):
        return "YES"

    # Check if lst2 is empty
    if not lst2:
        return "NO"

    # Check if any element of lst2 is even
    if any(num % 2 == 0 for num in lst2):
        return "YES"

    # If none of the above conditions are true, return "NO"
    return "NO"


