

def exchange(lst1, lst2):
    

    # Check if both lists are non-empty
    if not lst1 and not lst2:
        return "NO"

    # Create a set of even numbers from lst1
    even_nums = set(n for n in lst1 if n % 2 == 0)

    # Check if lst2 has any odd numbers
    for num in lst2:
        if num % 2 == 1:
            return "NO"

    # Check if lst1 has any odd numbers
    for num in lst1:
        if num % 2 == 1:
            return "NO"

    # If we reach this point, then all the numbers in lst1 and lst2 are even
    return "YES"


