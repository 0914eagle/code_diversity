def by_length(arr):
    
    # create a dictionary to map the numbers to their names
    num_to_name = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }

    # create a list to store the names
    names = []

    # loop through the array
    for num in arr:
        # check if the number is between 1 and 9 inclusive
        if 1 <= num <= 9:
            # if it is, add the name to the names list
            names.append(num_to_name[num])

    # reverse the names list
    names.reverse()

    return names


print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([]))
print(by_length([1, -1, 55]))
