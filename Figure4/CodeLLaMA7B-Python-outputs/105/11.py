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
        if i >= 1 and i <= 9:
            # append the result to the list
            result.append(str(i))
    # return the result
    return result


# test case
print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))  # ['One', 'One', 'Two', 'Two', 'Three', 'Four', 'Five', 'Eight']
print(by_length([]))  # []
print(by_length([1, -1, 55]))  # ['One']
