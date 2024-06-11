def pairs_sum_to_zero(l):
    
    # return True if there are two distinct elements in the list that sum to zero, and False otherwise.
    # Hint: keep track of which numbers have been checked.
    # You won't need to use the l variable above -- only the list that is passed into the function.
    # Also, don't forget to return True or False at the end.
    # iterate through the list
    # check if the element is in the list
    # if it is, return true
    # if it is not, add it to the list
    # return false
    # Your code here
    # iterate through the list
    for i in range(len(l)):
        # check if the element is in the list
        if l[i] in l:
            # if it is, return true
            return True
        # if it is not, add it to the list
        l.append(l[i])
    # return false
    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
