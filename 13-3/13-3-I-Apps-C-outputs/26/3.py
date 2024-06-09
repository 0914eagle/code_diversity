
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
                remove_lst.append(lst[i])

        # Remove the elements from the list
        for i in remove_lst:
            lst.remove(i)

        # Insert the elements at the same position, divided by 2, and the remainder
        for i in remove_lst:
            lst.insert(i // 2, i % 2)

    # Return the number of ones in the range l to r
    return sum(lst[l-1:r])

