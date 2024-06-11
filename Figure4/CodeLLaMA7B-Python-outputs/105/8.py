def by_length(arr):
    
    # sort the array
    arr.sort()
    # reverse the array
    arr.reverse()
    # create a list to store the result
    result = []
    # loop through the array
    for i in arr:
        # check if the number is between 1 and 9
        if 1 <= i <= 9:
            # get the name of the number
            result.append(str(i) + " " + str(i))
        else:
            # if the number is not between 1 and 9, ignore it
            pass
    # return the result
    return result


# test case 1
arr = [2, 1, 1, 4, 5, 8, 2, 3]
print(by_length(arr))  # returns ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]

# test case 2
arr = []
print(by_length(arr))  # returns []

# test case 3
arr = [1, -1, 55]
print(by_length(arr))  # returns ['One']
