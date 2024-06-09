
def solve(n, l, r):
    # Initialize an empty list to store the elements
    lst = []

    # Add the initial element to the list
    lst.append(n)

    # Iterate until all elements are either 0 or 1
    while True:
        # Initialize a flag to check if the list is modified
        modified = False

        # Iterate through the list and remove any element that is greater than 1
        for i in range(len(lst)):
            if lst[i] > 1:
                # Calculate the floor of the element divided by 2 and the modulus of the element divided by 2
                floor = lst[i] // 2
                mod = lst[i] % 2

                # Insert the floor and mod at the same position in the list
                lst.insert(i, floor)
                lst.insert(i + 1, mod)

                # Set the modified flag to True
                modified = True

        # If the list is not modified, break the loop
        if not modified:
            break

    # Return the sum of the elements in the range l to r
    return sum(lst[l - 1:r])

