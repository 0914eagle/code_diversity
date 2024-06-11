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
            result.append(str(i) + " " + "One" if i == 1 else str(i) + " " + "Two" if i == 2 else str(i) + " " + "Three" if i == 3 else str(i) + " " + "Four" if i == 4 else str(i) + " " + "Five" if i == 5 else str(i) + " " + "Six" if i == 6 else str(i) + " " + "Seven" if i == 7 else str(i) + " " + "Eight" if i == 8 else str(i) + " " + "Nine")
    return result


print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([]))
print(by_length([1, -1, 55]))
