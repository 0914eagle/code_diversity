def by_length(arr):
    
    # sort the array
    arr.sort()
    # reverse the array
    arr.reverse()
    # create an empty list to store the names
    names = []
    # loop through the array
    for i in arr:
        # check if the number is between 1 and 9
        if i >= 1 and i <= 9:
            # get the name of the number
            name = get_name(i)
            # append the name to the list
            names.append(name)
    # return the list
    return names

