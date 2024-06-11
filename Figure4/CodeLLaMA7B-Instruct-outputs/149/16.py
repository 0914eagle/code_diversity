

def sorted_list_sum(lst):
    

    # Create a new list to store the sorted and filtered words
    sorted_list = []

    # Iterate over the input list and filter out the words with odd lengths
    for word in lst:
        if len(word) % 2 == 0:
            sorted_list.append(word)

    # Sort the filtered words by length and then alphabetically
    sorted_list.sort(key=lambda x: (len(x), x))

    return sorted_list


