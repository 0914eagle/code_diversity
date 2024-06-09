
def solve(n, l, r):
    # Initialize an empty list to store the elements
    lst = []

    # Add the initial element to the list
    lst.append(n)

    # Iterate until all elements in the list are either 0 or 1
    while len(lst) > 0:
        # Initialize a new list to store the elements that will be removed
        remove_lst = []

        # Iterate through the list and remove any element that is greater than 1
        for i in range(len(lst)):
            if lst[i] > 1:
                # Remove the element and add it to the remove list
                remove_lst.append(lst[i])
                lst.pop(i)

        # Iterate through the remove list and insert the elements at the same position
        for i in range(len(remove_lst)):
            # Calculate the position to insert the element
            pos = int(remove_lst[i] / 2)

            # Insert the element at the position
            lst.insert(pos, remove_lst[i] % 2)

    # Return the total number of 1s in the range l to r
    return sum(lst[l-1:r])

