

def sorted_list_sum(lst):
    

    # create a new list to store the sorted and filtered words
    sorted_list = []

    # loop through the input list and filter out the words with odd lengths
    for word in lst:
        if len(word) % 2 == 0:
            sorted_list.append(word)

    # sort the list by length and then alphabetically
    sorted_list.sort(key=lambda x: (len(x), x))

    return sorted_list


