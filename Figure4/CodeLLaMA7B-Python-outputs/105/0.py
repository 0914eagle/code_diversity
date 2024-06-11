def by_length(arr):
    
    # sort the array
    arr.sort()
    # reverse the array
    arr.reverse()
    # create a list of names
    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    # create an empty list to store the names
    result = []
    # iterate through the array
    for i in arr:
        # check if the number is between 1 and 9
        if i >= 1 and i <= 9:
            # append the name to the result
            result.append(names[i - 1])
    # return the result
    return result


print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([]))
print(by_length([1, -1, 55]))
