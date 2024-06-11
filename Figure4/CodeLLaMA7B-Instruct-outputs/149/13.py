

def sorted_list_sum(lst):
    

    # Create a new list to store the sorted and filtered strings
    sorted_list = []

    # Iterate over the input list and append strings with even lengths to the new list
    for string in lst:
        if len(string) % 2 == 0:
            sorted_list.append(string)

    # Sort the new list by length and then alphabetically
    sorted_list.sort(key=lambda x: (len(x), x))

    return sorted_list


