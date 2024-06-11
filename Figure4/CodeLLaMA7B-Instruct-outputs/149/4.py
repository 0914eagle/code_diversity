

def sorted_list_sum(lst):
    

    # Create a new list to store the sorted and filtered strings
    sorted_list = []

    # Iterate over the input list and append the strings that have even lengths to the new list
    for word in lst:
        if len(word) % 2 == 0:
            sorted_list.append(word)

    # Sort the new list by length and then alphabetically
    sorted_list.sort(key=lambda x: (len(x), x))

    return sorted_list


