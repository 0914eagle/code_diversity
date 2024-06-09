
def solve(n, l, r):
    # Initialize an empty list to store the elements
    lst = []

    # Add the initial element to the list
    lst.append(n)

    # Iterate until all elements in the list are either 0 or 1
    while len(lst) > 0:
        # Initialize a new list to store the updated elements
        new_lst = []

        # Iterate through the list and perform the operations
        for i in lst:
            # If the element is greater than 1, remove it and insert its floor division by 2, modulo 2, and floor division by 2 again
            if i > 1:
                new_lst.append(i // 2)
                new_lst.append(i % 2)
                new_lst.append(i // 2)
            # Otherwise, just append the element to the new list
            else:
                new_lst.append(i)

        # Set the list to the updated list
        lst = new_lst

    # Return the total number of 1s in the range l to r
    return sum(lst[l-1:r])

