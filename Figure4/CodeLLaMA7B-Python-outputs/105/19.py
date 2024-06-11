def by_length(arr):
    
    # sort the array
    arr.sort()
    # reverse the array
    arr.reverse()
    # create a list to store the names
    names = []
    # loop through the array
    for i in arr:
        # if the number is between 1 and 9 inclusive
        if i >= 1 and i <= 9:
            # append the name to the list
            names.append(str(i) + " " + "One")
        # if the number is not between 1 and 9 inclusive
        else:
            # append the number to the list
            names.append(str(i))
    # return the list
    return names


# print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
# print(by_length([]))
# print(by_length([1, -1, 55]))


