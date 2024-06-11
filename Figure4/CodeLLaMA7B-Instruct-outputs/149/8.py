

def sorted_list_sum(lst):
    

    # create a new list to store the sorted and filtered strings
    sorted_list = []

    # loop through the input list and check the length of each string
    for string in lst:
        if len(string) % 2 == 0:
            # if the length is even, add the string to the sorted list
            sorted_list.append(string)

    # sort the list by length and then alphabetically
    sorted_list.sort(key=lambda x: (len(x), x))

    return sorted_list


