
def solve(n, l, r):
    # Initialize an empty list to store the elements
    lst = []

    # Add the initial element to the list
    lst.append(n)

    # Iterate until all elements are either 0 or 1
    while len(lst) > 0:
        # Initialize a new list to store the updated elements
        new_lst = []

        # Iterate through the list and perform the required operations
        for i in lst:
            if i > 1:
                # Remove the element and insert it at the same position and its half
                new_lst.append(i // 2)
                new_lst.append(i % 2)
                new_lst.append(i // 2)
            else:
                # If the element is 0 or 1, just append it to the new list
                new_lst.append(i)

        # Update the list with the updated elements
        lst = new_lst

    # Return the total number of 1s in the range l to r
    return sum(lst[l-1:r])

