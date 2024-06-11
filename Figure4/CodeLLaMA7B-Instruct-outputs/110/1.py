

def exchange(lst1, lst2):
    

    # Check if all the elements of lst1 are even
    if all(num % 2 == 0 for num in lst1):
        return "YES"

    # Check if lst2 is empty
    if not lst2:
        return "NO"

    # Check if lst2 has any odd elements
    if any(num % 2 != 0 for num in lst2):
        return "NO"

    # Exchange elements between lst1 and lst2
    for i in range(len(lst1)):
        if lst1[i] % 2 != 0:
            lst1[i], lst2[-1] = lst2[-1], lst1[i]
            lst2.pop()
            break

    # Check if all the elements of lst1 are even now
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    else:
        return "NO"


