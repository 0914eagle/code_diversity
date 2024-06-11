

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

    # Check if lst2 has any even numbers that are not in lst1
    for num in lst2:
        if num not in even_nums:
            return "YES"

    # If we reach this point, it means that lst2 only has even numbers that are
    # also in lst1, so we can exchange elements between the two lists
    return "YES"


