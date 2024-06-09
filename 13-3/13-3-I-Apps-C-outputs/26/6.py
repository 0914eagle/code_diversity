
def solve(n, l, r):
    # Initialize an empty list to store the elements
    lst = []

    # Add the initial element to the list
    lst.append(n)

    # Iterate until all elements in the list are either 0 or 1
    while len(lst) > 0:
        # Initialize a new list to store the elements that need to be removed
        remove_lst = []

        # Iterate through the list and find elements that are greater than 1
        for i in range(len(lst)):
            if lst[i] > 1:
                # Remove the element from the list
                remove_lst.append(lst[i])

        # Iterate through the list of elements to be removed and insert them back into the list
        for i in range(len(remove_lst)):
            # Calculate the position to insert the element
            pos = int(remove_lst[i] / 2)

            # Insert the element into the list at the calculated position
            lst.insert(pos, remove_lst[i] % 2)

        # Remove all elements that are greater than 1 from the list
        for i in range(len(remove_lst)):
            lst.remove(remove_lst[i])

    # Return the total number of 1s in the range l to r
    return sum(lst[l-1:r])

