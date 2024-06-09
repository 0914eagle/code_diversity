
def solve(n, l, r):
    # Initialize an empty list to store the elements
    lst = []

    # Add the initial element to the list
    lst.append(n)

    # Iterate until all elements in the list are either 0 or 1
    while True:
        # Initialize a flag to check if the list has only 0s and 1s
        flag = True

        # Iterate through the list and perform the operations
        for i in range(len(lst)):
            # If the element is greater than 1, remove it and insert its half and the remainder sequentially
            if lst[i] > 1:
                # Calculate the half and the remainder of the element
                half = lst[i] // 2
                remainder = lst[i] % 2

                # Insert the half and the remainder at the same position
                lst.insert(i, half)
                lst.insert(i + 1, remainder)

                # Set the flag to False to indicate that the list has changed
                flag = False

        # If the list has only 0s and 1s, break the loop
        if flag:
            break

    # Return the total number of 1s in the range l to r
    return sum(lst[l - 1:r])

