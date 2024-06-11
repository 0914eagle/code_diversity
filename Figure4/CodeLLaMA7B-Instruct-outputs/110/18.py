

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

    # If we reach this point, it means that both lists are even,
    # so we can exchange elements between them to make lst1 even
    return "YES"


