

def sorted_list_sum(lst):
    

    # create a new list to store the sorted and filtered words
    sorted_list = []

    # loop through the input list and check the length of each word
    for word in lst:
        if len(word) % 2 == 0:
            # if the length is even, add the word to the sorted list
            sorted_list.append(word)

    # sort the list by length and then alphabetically
    sorted_list.sort(key=lambda x: (len(x), x))

    return sorted_list


