

def exchange(lst1, lst2):
    

    # Check if both lists are non-empty
    if not lst1 and not lst2:
        return "NO"

    # Create a set of even numbers from lst1
    even_nums = set(n for n in lst1 if n % 2 == 0)

    # Check if lst2 contains any odd numbers
    for num in lst2:
        if num % 2 == 1:
            return "NO"

    # Check if lst1 can be made entirely of even numbers by exchanging elements with lst2
    for num in lst1:
        if num not in even_nums:
            return "NO"

    return "YES"


